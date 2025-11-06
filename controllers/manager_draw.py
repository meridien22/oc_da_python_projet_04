import math
import copy
import random
from controllers import ManagerTool
from models import Match


class ManagerDraw:
    def __init__(self, tournament):
        self.tournament = tournament
        self.list_ = []
        self.list_forbidden = []
        self.manager_tool = ManagerTool()

    def get_pairs(self, combination):
        """Retourne les paires d'éléments d'une liste
        L'ordre est respecté au maximimum
        Les paires interdites sont évités si possible
        Retourne une liste de paire ou None en cas d'échec"""
        list_copy = copy.deepcopy(combination)
        list_pair = []
        while len(list_copy) > 0:
            element_base = list_copy[0]
            for index, element in enumerate(list_copy):
                # on veut commencer au 2ᵉ élément de la liste
                index += 1
                # si on sort de la liste, on sort du for avec le break
                # on vide la list list_copy pour provoquer la sortie du while
                # on vide la list_pair pour provoquer un échec du tirage
                if index > len(list_copy) - 1:
                    list_copy = []
                    list_pair = []
                    break
                tuple_ = (element_base, list_copy[index])
                if tuple_ not in self.list_forbidden:
                    # print(f"tuple : {tuple_} => ok")

                    list_pair.append(tuple_)
                    list_copy.pop(index)
                    list_copy.pop(0)
                    break
                else:
                    pass
                    # print(f"tuple : {tuple_} => no ok")
        if len(list_pair) > 0:
            return list_pair
        else:
            return None

    def get_combination(self, list_):
        """Retourne une liste avec toutes pes combinaisons possibles des éléments sans doublon"""
        list_copy = copy.deepcopy(list_)
        combination = []
        number_possible = math.factorial(len(list_copy))
        # on met la combinaison présente par défaut en premier dans la liste des combinaisons
        combination.append(copy.deepcopy(list_copy))
        while len(combination) < number_possible:
            random.shuffle(list_copy)
            if list_copy not in combination:
                combination.append(copy.deepcopy(list_copy))
        return combination

    def replace_end_list(self, list_, end_list_):
        """Remplace la fin d'une liste par une autre liste"""
        list_[-len(end_list_):] = end_list_

    def get_list_combination(self, number_end_element):
        """Retoune une liste avec toutes les combinaisons possibles des x derniers éléments de la liste"""
        list_copy = copy.deepcopy(self.list_)
        list_end = self.list_[-number_end_element:]
        list_combination = []
        for combination in self.get_combination(list_end):
            self.replace_end_list(list_copy, combination)
            list_combination.append(copy.deepcopy(list_copy))
        # print(f"list_combination : {list_combination}")
        return list_combination

    def update_list_tournament(self):
        match_forbidden_list = []
        id_national_list = []

        for player in self.tournament.player_list:
            id_national_list.append(player["id_national"])
            for opponent in player["opponent_list"]:
                match_forbidden_list.append((player["id_national"], opponent))

        self.list_ = id_national_list
        self.list_forbidden = match_forbidden_list

    def get_draw(self):
        """Retoune un nouveau tirage"""
        # si c'est le premier tour, on mélange les joueurs aléatoirement
        if len(self.tournament.round_list) == 0:
            random.shuffle(self.tournament.player_list)
        # sinon on trie les joueurs en fonction de leurs scores
        else:
            self.tournament.player_list.sort(key=lambda element: element["score"], reverse=True)
        self.update_list_tournament()
        end_number = 3
        end_draw = False
        list_pair = []
        while not end_draw:
            for combination in self.get_list_combination(end_number):
                if end_draw:
                    break
                # print(f"combination : {combination}")
                list_pair = self.get_pairs(combination)
                if list_pair:
                    end_draw = True
            end_number += 1

        match_list = []

        for pair in list_pair:
            match_list.append(Match(pair[0], pair[1]))

        self.manager_tool.update_opponent_list(self.tournament, match_list)

        return match_list
