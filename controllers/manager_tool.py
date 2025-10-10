import random
import datetime
import re
from views.display_choice import *
from models import *


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
        continue_ = True
        # si le nombre de joueurs inscrits est pair, il faut qu'il reste au moins
        # 2 joueurs de disponible car sinon on tombe sur un nombre de joueurs
        # inscrits au tournoi impair
        if self.player_register_even_number(tournament):
            if self.number_player_available_for_inscription(tournament, player_list_all) >= 2:
                continue_ = True
            else:
                continue_ = False
        return continue_

    def player_register_even_number(self, tournament):
        """Renvoi True si le nombre de joueurs inscrit est pair"""
        return len(tournament.player_list) % 2 == 0

    def number_player_available_for_inscription(self, tournament, player_list):
        """Renvoi le nombre de joueurs qui peuvent encore s'inscrire dans le tournoi"""
        number_player_available = len(player_list)
        for player in tournament.player_list:
            if player["id_national"] in self.get_list_id_national(tournament):
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

    def last_round_finish(self, tournament):
        last = self.is_max_round(tournament)
        progress = self.round_in_progress(tournament)
        if last and not progress:
            return True
        else:
            return False

    def check_inscriptin_open(self, tournament, player_list_all):
            if tournament is None:
                return "2"
            if len(tournament.round_list) > 0:
                return "3"
            if len(tournament.player_list) == len(player_list_all):
                return "4"
            if not self.list_player_compatible_with_number_round(player_list_all):
                return "7"
            return 0

    def get_list_id_national(self, tournament):
        """Renvoi une liste de tous les id_national des joueurs inscrit au tournoi"""
        id_national_list = []
        for player in tournament.player_list:
            id_national_list.append(player["id_national"])
        return id_national_list

    def get_match(self, tournament):
        """" Renvoi les matches d'un tour
        1er tour : tirage aléatoire
        tour suivant : tirage score => tirage logique => tirage aléatoire"""

        # si c'est le premier tour, on mélange les joueurs aléatoirement
        if len(tournament.round_list) == 0:
            random.shuffle(tournament.player_list)
        # sinon on trie les joueurs en fonction de leurs scores
        else:
            tournament.player_list.sort(key=lambda element: element["score"])

        draw = self.get_draw(tournament)
        index_modifier = 1
        while draw == "Echec":
            draw = self.get_draw(tournament)
            # tirage logique en essayant de respecter le plus possible
            # le tri par score
            if index_modifier < len(tournament.player_list):
                # on soustrait à la liste le joueur qui correxpond
                # à l'index modifieur
                player_modifier = tournament.player_list.pop(index_modifier)
                # on l'insert dans la liste à la position suivante
                tournament.player_list.insert(index_modifier + 1, player_modifier)
                index_modifier += 1
            # tirage aléatoire car la méthode précédnte a échoué
            else:
                random.shuffle(tournament.player_list)

        return draw

    def get_draw(self, tournament):
        """Propose un tirage pour un tour"""
        index_player_1 = 0
        index_player_2 = 1
        match_list = []
        while index_player_2 < len(tournament.player_list):
            index_search = index_player_2
            player_1 = tournament.player_list[index_player_1]
            player_2 = tournament.player_list[index_player_2]
            # cas où le match a déjà été joué
            while player_2["id_national"] in player_1["opponent_list"]:

                # cas ou l'algorithme n'a pas réussi à proposer
                # une combinaison cohérente car
                # l'index de recherce est arrivé au bout de la liste
                if index_search + 1 == len(tournament.player_list):
                    return "Echec"
                # on soustrait à la liste le joueur qui vient après le joueur 2
                player_next = tournament.player_list.pop(index_search + 1)
                # on l'insert dans la liste après le joueur 1
                tournament.player_list.insert(index_player_1 + 1, player_next)
                # on crée un nouveau match pour pouvoir tester
                # s'il a déjà été joué ou non
                player_1 = tournament.player_list[index_player_1]
                player_2 = tournament.player_list[index_player_2]
                # on incrémente l'index de recherche de 1 pour aller chercher
                # le prochain candididat si le match a déjà été joué
                index_search += 1
            match = Match(player_1["id_national"], player_2["id_national"])
            match_list.append(match)
            index_player_1 += 2
            index_player_2 += 2
        # sortie du while sans avoir rencontré d'échec,
        # on met à jour la liste des adversaires des joueurs
        self.update_opponent_list(tournament, match_list)
        return match_list

    def update_opponent_list(self, tournament, match_list):
        for match in match_list:
            for player_tournament in tournament.player_list:
                if player_tournament["id_national"] == match.player_1:
                    player_tournament["opponent_list"].append(match.player_2)
                else:
                    player_tournament["opponent_list"].append(match.player_1)

    def add_round(self, tournament):
        # s'il exsite un tour on le finit
        if len(tournament.round_list) > 0:
            roud_last = tournament.round_list[-1]
            roud_last.finish()

        match_list = self.get_match(tournament)
        round_ = Round(tournament.round_list, match_list)
        tournament.round_list.append(round_)

    def is_max_round(self, tournament):
        """Retourne True si le nombre maximum de tours du tournoi a été atteint"""
        return len(tournament.round_list) == tournament.round_number
