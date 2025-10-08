import os
import random
import datetime
import re
from views import *
from models import *

class Controller:

    # séquence de caractère à taper dans la recherche pour obtenir tous les jouers
    FIND_ALL = "*"

    def __init__(self, display):
        self.display = display
        self.tool = Tool()

    def get_main_menu(self, tournament):
        menu = MenuMain()
        return menu.execute(tournament)

    def get_information(selfself, code):
        menu = InformationUser()
        menu.execute(code)

    def get_menu_inscription(self, tournament, player_list):
        action_dict = {}
        len_ = len(tournament.player_list)
        registration = False
        close = False

        # si le nombre de joueurs inscrits est pair, il faut qu'il reste au moins
        # 2 joueurs de disponible car sinon on tombe sur un nombre de joueurs
        # inscrits au tournoi impair
        number_player_available = len(player_list)
        if len_ % 2 == 0:
            for player in tournament.player_list:
                if player["id_national"] in tournament.id_national_list:
                    number_player_available -= 1
            if number_player_available >= 2:
                registration = True
        else:
            registration = True

        # s'il y a des joueurs inscrits en nombre pair,
        # et si nombre de joueurs >= 2 x le nombre de tours
        # alors clôture possible
        if len_ > 0 and len_ % 2 == 0 and len_ >= tournament.DEFAULT_NUMBER_ROUND * 2:
            close = True

        menu = MenuInscription()
        return menu.execute(registration, close, tournament.name)

    def get_tournament(self):
        tournament_id = self.tool.get_national_id()
        menu = MenuTournament()
        value_dict = menu.execute()
        return Tournament(tournament_id,
                          value_dict["name"],
                          value_dict["location"],
                          "", "")

    def get_tournament_choice(self, tournament_list):
        tournamet_display = []
        for tournament in tournament_list:
            tournamet_display.append(tournament)
        menu = MenuTournamentChoice()
        return menu.execute(tournamet_display)

    def get_new_player(self):
        player_id_national = self.tool.get_national_id()
        menu = MenuNewPlayer()
        value_dict = menu.execute()
        return Player(value_dict["name"], value_dict["fist_name"], "", player_id_national)

    def get_inscription(self, tournament, player_list):
        menu = MenuHint()
        hint = menu.execute(tournament.name)

        player_filter_inscription_list = []
        # on contrôle d'abord que le joueur ne soit pas déjà inscrit
        for player in player_list:
            if player.id_national not in tournament.id_national_list:
                player_filter_inscription_list.append(player)

        # on fait une recherche dans le nom et dans le prénom si demandé
        player_filter_hint_list = []
        if hint != self.FIND_ALL:
            hint = re.escape(hint)
            for player in player_filter_inscription_list:
                find_name = re.search(hint, player.name, re.IGNORECASE)
                find_first_name = re.search(hint, player.first_name, re.IGNORECASE)
                if find_name or find_first_name:
                    player_filter_hint_list.append(player)
        else:
            player_filter_hint_list = player_filter_inscription_list

        # si la recherche ne renvoie aucun résultat, on renvoie la premmière liste filtrée
        if len(player_filter_hint_list) == 0:
            player_filter_hint_list = player_filter_inscription_list

        menu = MenuInscriptionPlayer()
        return  player_filter_hint_list[menu.execute(tournament.name, player_filter_hint_list)]

    def get_player_register(self, player_list, tournament):
        player_display_list = []
        for player_id_national in tournament.id_national_list:
            player = self.tool.get_player_from_id(player_list, player_id_national)
            row = [player.first_name, player.name, player.date_birth, player.id_national]
            player_display_list.append(row)

        menu = MenuPlayerRegister()
        return menu.execute(tournament.name, player_display_list)

    def get_player_other(self, player_list, tournament):
        player_display_list = []
        for player in player_list:
            if player.id_national not in tournament.id_national_list:
                row = [player.first_name, player.name, player.date_birth, player.id_national]
                player_display_list.append(row)

        menu = MenuPlayerOther()
        return menu.execute(tournament.name, player_display_list)

    def get_player_full(self, player_list):
        player_display_list = []
        for player in player_list:
            row = [player.first_name, player.name, player.date_birth, player.id_national]
            player_display_list.append(row)

        menu = MenuPlayerFull()
        return menu.execute(player_display_list)

    def get_tournament_full(self, tournament_list):
        tournament_display_list = []
        for tournament in tournament_list:
            round_number = len(tournament.round_list)
            player_number = len(tournament.player_list)
            row = [tournament.name, tournament.place, round_number, player_number]
            tournament_display_list.append(row)

        menu = MenuTournamentFull()
        return menu.execute(tournament_display_list)

    def get_menu_round(self, tournament, player_list):
        round_ = tournament.round_list[-1]

        menu = MenuRound()
        return menu.execute(tournament.name, round_.name)

    def get_enter_result(self, tournament, player_list):
        round_ = tournament.round_list[-1]
        action_dict = {}
        match_for_result_list = []
        for index, match in enumerate(round_.match_list):
            if match.winner is None:
                match_for_result_list.append(match)

        for index, match in enumerate(match_for_result_list):
            player_1 = self.tool.get_player_from_id(player_list, match.player_1)
            player_2 = self.tool.get_player_from_id(player_list, match.player_2)
            action_dict[str(index + 1)] = str(player_1) + " contre " + str(player_2)

        menu = MenuEnterResult()
        match_index = menu.execute(action_dict, tournament.name, round_.name)
        match = match_for_result_list[match_index]

        action_dict = {}
        player_1 = self.tool.get_player_from_id(player_list, match.player_1)
        player_2 = self.tool.get_player_from_id(player_list, match.player_2)
        action_dict["1"] = player_1
        action_dict["2"] = player_2
        action_dict["3"] = "Match nul"

        menu = MenuEnterMacthResult()
        choice = menu.execute(action_dict, tournament.name, round_.name)

        match choice:
            case "1":
                match.winner = player_1.id_national
            case "2":
                match.winner = player_2.id_national
            case "3":
                match.winner = 0

    def get_round_resume(self, tournament, player_list):
        round_display_list = []
        for round_ in tournament.round_list:
            row = [round_.name, round_.date_time_start, round_.date_time_end, len(round_.match_list)]
            round_display_list.append(row)

        match_display = []
        roud_last = tournament.round_list[-1]
        for match in roud_last.match_list:
            player_1 = self.tool.get_player_from_id(player_list, match.player_1)
            player_2 = self.tool.get_player_from_id(player_list, match.player_2)
            winner = self.tool.get_player_from_id(player_list, match.winner)
            row = [player_1, player_2, winner]
            match_display.append(row)

        menu = MenuRoundREsume()
        return menu.execute(tournament.name, roud_last.name, round_display_list, match_display)

class Tool:

    def set_tile(self, id_menu, title):
        display_parameters[id_menu]["title"] = title

    def get_national_id(self):
        letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
        random.shuffle(letter_list)
        letter_1 = letter_list[0]
        lettre_2 = letter_list[1]
        number = datetime.datetime.now().strftime("%H%M%S")
        return letter_1 + lettre_2 + number

    def get_list_player_from_hint(self, hint, player_list):
        player_hint = []
        hint = re.escape(hint)
        for player in player_list:
            match = False
            if re.search(hint, player.name, re.IGNORECASE):
                match = True
            if re.search(hint, player.first_name, re.IGNORECASE):
                match = True
            if match:
                player_hint.append(player)
        if len(player_hint) == 0:
            return player_list
        else:
            return player_hint

    def tournament_to_activate(self, tournament_list):
        if len(tournament_list) > 0:
            return True
        else:
            return False

    def inscription_finished(self, tournament):
        if len(tournament.player_list) > 0 and len(tournament.round_list) > 0:
            return True
        else:
            return False

    def round_in_progress(self, tournament):
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
            return 0

    def all_rounf_played(self, tournament):
        if len(tournament.round_list) == tournament.DEFAULT_NUMBER_ROUND:
            if self.round_in_progress(tournament):
                return False
            else:
                return True
        else:
            return False

    def get_player_from_id(self, player_list, id_national):
        for player in player_list:
            if player.id_national == id_national:
                return player
        return None