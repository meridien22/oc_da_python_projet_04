import random
import re
import datetime
import os
import json
from views import InformationUser, MenuListPaginated
from models import Tournament, Player, Round


class ManagerTool:

    # Répertoire où seront enregistrés les tournois
    DIRECTORY_TOURNAMENT = "data\\tournament"
    # Répertoire où seront enregistrés les joueurs
    JSON_PLAYER = "data\\players.jsonl"

    def get_information(self, code, parameter=None):
        """Lance l'affichage d'un message avec un contenu précis"""
        menu = InformationUser()
        menu.execute(code, parameter)

    def get_message(self, code):
        """Affiche le message qui correspond au code"""
        return InformationUser.get_message(code)

    def get_list_paginated(self, title, header_list, list_, number_per_page, clear=True):
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
            choice = menu.execute(title, header_list, list_extract, page, page_full, clear)
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
        """Retourne un objet Player à partir d'un ID national"""
        for player in player_list:
            if player.id_national == id_national:
                return player
        return None

    def get_national_id(self):
        """Génère aléatoirement un ID national"""
        letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
        random.shuffle(letter_list)
        letter_1 = letter_list[0]
        lettre_2 = letter_list[1]
        number = datetime.datetime.now().strftime("%H%M%S")
        return letter_1 + lettre_2 + number

    def get_player_from_hint(self, hint, player_list):
        """Retourne une liste de joueur correspondant au critère de recherche"""
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
        """Retourne True s'il y a possibilité d'activer un tournoi"""
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
        """Renvoi True si le dernier tour est terminé"""
        last = self.is_max_round(tournament)
        progress = self.round_in_progress(tournament)
        if last and not progress:
            return True
        else:
            return False

    def check_inscriptin_open(self, tournament, player_list_all):
        """Renvoi True s'il est possible de continuer les inscriptions"""
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

    def update_opponent_list(self, tournament, match_list):
        """Met à joueur la liste des adversaires d'un joueur"""
        for match in match_list:
            for player_tournament in tournament.player_list:
                if player_tournament["id_national"] == match.player_1:
                    player_tournament["opponent_list"].append(match.player_2)
                elif player_tournament["id_national"] == match.player_2:
                    player_tournament["opponent_list"].append(match.player_1)

    def add_round(self, tournament, match_list):
        """Ajoute un nouveau tour au tournoi"""
        round_name = self.get_name_next_round(tournament)
        round_ = Round(round_name, match_list)
        tournament.round_list.append(round_)

    def is_max_round(self, tournament):
        """Retourne True si le nombre maximum de tours du tournoi a été atteint"""
        return len(tournament.round_list) == tournament.round_number

    def get_name_next_round(self, tournament):
        """Retourne le nom du dernier tour"""
        round_number = len(tournament.round_list) + 1
        return f"Tour {round_number}"

    def save_tournamen(self, tournament):
        """Sauvegarde un tournoi dans un fichier json"""
        dump_str = tournament.to_dict()
        json_file = os.path.join(self.DIRECTORY_TOURNAMENT, f"{tournament.id}.json")
        with open(json_file, "w", encoding='utf-8') as f:
            json.dump(dump_str, f, ensure_ascii=False, indent=4)

    def load_all_tournament(self, tournament_list):
        """Charge des tournois à partir de fichiers json"""
        directory_list = os.listdir(self.DIRECTORY_TOURNAMENT)
        for element in directory_list:
            path_element = os.path.join(self.DIRECTORY_TOURNAMENT, element)
            if os.path.isfile(path_element):
                with open(path_element, 'r', encoding='utf-8') as file:
                    json_str = json.load(file)
                    tournament_list.append(Tournament.from_dict(json_str))

    def save_all_player(self, player_list):
        """Sauvegarde tous les joueurs dans un fichier json"""
        with open(self.JSON_PLAYER, 'w', encoding='utf-8') as file:
            for player in player_list:
                json_line = json.dumps(player.to_dict(), ensure_ascii=False)
                file.write(json_line + '\n')

    def load_player(self, player_list):
        """Charge des joueurs contenus dans un fichier json"""
        with open(self.JSON_PLAYER, 'r', encoding='utf-8') as file:
            for line in file:
                json_str = json.loads(line)
                player_list.append(Player.from_dict(json_str))

    def get_list_tuple(self, tournament, player_list):
        """Retourne un tuple contenant deux listes, chacune contenant
        deux éléments : un joueur et un score"""
        list_tuple = []
        for round_ in tournament.round_list:
            for match in round_.match_list:
                player_1 = self.get_player_from_id(player_list, match.player_1)
                player_2 = self.get_player_from_id(player_list, match.player_2)
                score_1 = self.get_score_from_id(tournament, match.player_1)
                score_2 = self.get_score_from_id(tournament, match.player_2)
                list_tuple.append(([player_1, score_1], [player_2, score_2]))
        return list_tuple

    def get_score_from_id(self, tournament, id_national):
        """Retourne le score d'un joueur à partir de son id national"""
        for player in tournament.player_list:
            if player["id_national"] == id_national:
                return player["score"]
        return None
