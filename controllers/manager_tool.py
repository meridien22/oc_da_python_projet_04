import random
import datetime
import re
from views.display_choice import *
from models.tournament import Tournament


class ManagerTool:

    def get_information(self, code, parameter=None):
        """Lance l'affichage d'un message avec un contenu précis"""
        menu = InformationUser()
        menu.execute(code, parameter)

    def get_list_paginated(self, title, header_list, list_, number_per_page):
        """Permet d'afficher une longue liste en plusieurs pages"""
        # Index de départ de la liste pour la page en cours
        index_start = 0
        # Index de fin de la liste pour la page en cours
        index_end = 0
        # La première page est la page 1
        page = 1
        # On fait une division entière de la longeur de la liste par le nombre d'éléments que l'on veut
        # afficher par page. Le quotient représente le nombre de fois que l'on peut afficher une
        # page complète et le reste représente la dernière page
        part, rest = divmod(len(list_), number_per_page)
        if rest > 0:
            rest = 1
        else:
            rest = 0
        page_full = part + rest

        # tant que l'index de fin ne dépasse pas la longueur de la liste
        while index_end < len(list_):
            # On extrait de la liste la partie qui nous intéresse
            # On faisant cela, on perd les index d'origine
            index_end = index_start + number_per_page
            list_extract = list_[index_start:index_end]
            menu = MenuListPaginated()
            choice = menu.execute(title, header_list, list_extract, page, page_full)
            # Si le choix est "s" on va à la page suivante
            if choice == "s":
                index_start += number_per_page
                page += 1
            # Si le choix est "r" ou si on est à la dernière page, on repart au début
            if choice == "r" or page == page_full + 1:
                index_start = 0
                index_end = 0
                page = 1
            # Si le choix est "a" on interrompt la procédure d'inscription
            if choice == "a" or page == page_full + 1:
                break

    def get_player_from_id(self, player_list, id_national):
        for player in player_list:
            if player.id_national == id_national:
                return player
        return None

    def get_national_id(self):
        letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
        random.shuffle(letter_list)
        letter_1 = letter_list[0]
        lettre_2 = letter_list[1]
        number = datetime.datetime.now().strftime("%H%M%S")
        return letter_1 + lettre_2 + number

    def get_player_from_hint(self, hint, player_list):
        hint = re.escape(hint)
        player_filter_hint_list = []
        for player in player_list:
            find_name = re.search(hint, player.name, re.IGNORECASE)
            find_first_name = re.search(hint, player.first_name, re.IGNORECASE)
            find_id_national = re.search(hint, player.id_national, re.IGNORECASE)
            if find_name or find_first_name or find_id_national:
                player_filter_hint_list.append(player)

        return player_filter_hint_list

    def tournament_to_activate(self, tournament_list):
        if len(tournament_list) > 0:
            return True
        else:
            return False

    def list_player_compatible_with_number_round(self, player_list):
        """Renvoi True si le nombre de joueurs est compatible avec le nombre de tour du tournoi"""
        # si nombre de joueurs >= 2 x le nombre de tours
        if len(player_list) >= Tournament.DEFAULT_NUMBER_ROUND * 2:
            return True
        else:
            return False

    def inscriptipn_can_continue(self, tournament, player_list_all):
        """Renvoi True s'il est possible d'inscrire des joueurs supplémentaires dans le tournoi"""
        len_ = len(tournament.player_list)
        continue_ = True
        # si le nombre de joueurs inscrits est pair, il faut qu'il reste au moins
        # 2 joueurs de disponible car sinon on tombe sur un nombre de joueurs
        # inscrits au tournoi impair
        if len_ % 2 == 0:
            if self.number_player_available_for_inscription(tournament, player_list_all) >= 2:
                continue_ = True
            else:
                continue_ = False
        return continue_

    def number_player_available_for_inscription(self, tournament, player_list):
        """Renvoi le nombre de joueurs qui peuvent encore s'inscrire dans le tournoi"""
        number_player_available = len(player_list)
        for player in tournament.player_list:
            if player["id_national"] in tournament.id_national_list:
                number_player_available -= 1
        return number_player_available

    def round_in_progress(self, tournament):
        """Renvoi True s'il y a un tour en cours dans le tournoi"""
        in_progress = False
        if len(tournament.round_list) > 0:
            round_ = tournament.round_list[-1]
            for match in round_.match_list:
                if match.winner is None:
                    in_progress = True
        return in_progress

    def check_inscriptin_open(self, tournament, player_list_all):
            if tournament is None:
                return 2
            if len(tournament.round_list) > 0:
                return 3
            if len(tournament.player_list) == len(player_list_all):
                return 4
            if not self.list_player_compatible_with_number_round(player_list_all):
                return 7
            return 0