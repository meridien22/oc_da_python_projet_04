import os
import random
import datetime
import re
from views import *
from models import *

class Controller:

    # séquence de caractère à taper dans la recherche pour obtenir tous les jouers
    FIND_ALL = "***"

    def __init__(self, display):
        self.display = display
        self.tool = Tool()

    # def get_menu_choice(self, id_menu):
    #     self.display.configure(display_parameters[id_menu])
    #     return self.display.get_input_choice()
    #
    # def get_menu_input(self, id_menu):
    #     self.display.configure(display_parameters[id_menu])
    #     return self.display.get_input()
    #
    # def get_confirmation(self):
    #     self.display.configure(display_parameters["50"])
    #     return self.display.get_confirmation()
    #
    # def get_list_tournament(self, tournament_liste):
    #     parameter = display_parameters["20"]
    #     action_dict = {}
    #
    #     for index, tournament in enumerate(tournament_liste):
    #         action_dict[str(index + 1)] = tournament.name
    #
    #     parameter["actions"] = action_dict
    #     self.display.configure(parameter)
    #     return self.display.get_input_choice()
    #
    # def get_list_player(self, player_list_hint, player_list_all):
    #     parameter = display_parameters["41"]
    #     action_dict = {}
    #
    #     for index, player in enumerate(player_list_all):
    #         if player in player_list_hint:
    #             action_dict[str(index + 1)] = player.name
    #
    #     parameter["actions"] = action_dict
    #     self.display.configure(parameter)
    #     return self.display.get_input_choice()
    #
    # def get_list_round_match(self, tournament_active):
    #     parameter = display_parameters["100"]
    #     parameter["content"] = tournament_active.get_rounds_matchs()
    #     self.display.configure(parameter)
    #     return self.display.get_input()

    def get_main_menu(self):
        actions = {
            "1": "Créer ou reprendre un tournoi",
            "2": "Saisir un nouveau joueur",
            "3": "Lister tous les joueurs",
            "4": "Lister tous les tournois",
            "99": "Quitter"
        }
        self.display.clear()
        self.display.set_title("CHESS MASTER PRO ULTIMATE")
        self.display.set_actions(actions)
        self.display.prompt = "Entrez le numéro de votre choix : "
        return self.display.get_input_choice()

    def get_menu_inscription(self, tournament, player_list):
        action_dict = {}
        len_ = len(tournament.player_list)

        # si le nombre de joueurs inscrits est pair, il faut qu'il reste au moins
        # 2 joueurs de disponible car sinon on tombe sur un nombre de joueurs
        # inscrits au tournoi impair
        number_player_available = len(player_list)
        if len_ % 2 == 0:
            for player in tournament.player_list:
                if player["id_national"] in tournament.id_national_list:
                    number_player_available -= 1
            if number_player_available >= 2:
                action_dict["1"] = "Inscrire un joueur"
        else:
            action_dict["1"] = "Inscrire un joueur"

        # s'il y a des joueurs inscrits en nombre pair, clôture possible
        if len_> 0 and len_ % 2 == 0:
            action_dict["2"] = "Clôturer les inscriptions"

        action_dict["3"] = "Liste des joueurs inscrits"
        action_dict["4"] = "Liste des autres joueurs"
        action_dict["0"] = "Retour au menu principal"

        self.display.clear()
        self.display.set_title(f"{tournament.name} : MENU INSCRIPTION")
        self.display.set_actions(action_dict)
        self.display.prompt = "Entrez le numéro de votre choix : "
        return self.display.get_input_choice()

    def get_inscription(self, tournament, player_list):
        self.display.min_character = 3
        self.display.clear()
        self.display.set_title(f"{tournament.name} : INSCRIPTION - RECHERCHE")
        self.display.prompt = "Entrez le nom ou une partie du nom du jouer (tapez *** pour lister tout les joueurs) : "
        hint = self.display.get_input()

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

        self.display.clear()
        self.display.set_title(f"{tournament.name} : INSCRIPTION - JOUEUR")
        action_dict = {}
        # on crée le menu
        for index, player in enumerate(player_filter_hint_list):
            action_dict[str(index + 1)] = player.name
        self.display.set_actions(action_dict)
        self.display.prompt = "Entrez le joueur de votre choix : "
        choice = self.display.get_input_choice()

        return  player_filter_hint_list[int(choice) - 1]

    def get_player_register(self, player_list, tournament):
        player_display_list = []
        for player_id_national in tournament.id_national_list:
            player = self.tool.get_player_from_id(player_list, player_id_national)
            row = [player.first_name, player.name, player.date_birth, player.id_national]
            player_display_list.append(row)

        self.display.clear()
        self.display.min_character = 0
        self.display.set_title(f"{tournament.name} : JOUEURS INSCRITS")
        self.display.set_content(player_display_list)
        self.display.prompt = "Tapez sur une touche pour continuer."
        return self.display.get_input()

    def get_player_other(self, player_list, tournament):
        player_display_list = []
        for player in player_list:
            if player.id_national not in tournament.id_national_list:
                row = [player.first_name, player.name, player.date_birth, player.id_national]
                player_display_list.append(row)

        self.display.clear()
        self.display.min_character = 0
        self.display.set_title(f"{tournament.name} : JOUEURS DISPONIBLES")
        self.display.set_content(player_display_list)
        self.display.prompt = "Tapez sur une touche pour continuer."
        return self.display.get_input()

    def get_menu_round(self, tournament, player_list):
        round_ = tournament.round_list[-1]
        actions = {
            "1": "Saisir les résultats",
            "2": "Résumé des tours",
            "0": "Retour au menu principal"
        }
        self.display.clear()
        self.display.set_title(f"{tournament.name} {round_.name}")
        self.display.set_actions(actions)
        self.display.prompt = "Entrez le numéro de votre choix : "
        return self.display.get_input_choice()

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
            player_1 = player_1
            player_2 = player_2
            action_dict[str(index + 1)] = player_1 + " contre " + player_2

        self.display.clear()
        self.display.set_title(f"{tournament.name} - {round_.name} - SAISIE DES RESULTATS 1/2")
        self.display.set_actions(action_dict)
        self.display.prompt = "Sélectionnez un match à encoder : "
        choice = self.display.get_input_choice()
        match_index = int(choice) - 1
        match = match_for_result_list[match_index]

        action_dict = {}
        player_1 = self.tool.get_player_from_id(player_list, match.player_1)
        player_2 = self.tool.get_player_from_id(player_list, match.player_2)
        action_dict["1"] = player_1
        action_dict["2"] = player_2
        action_dict["3"] = "Match nul"
        self.display.clear()
        self.display.set_title(f"{tournament.name} - {round_.name} - SAISIE DES RESULTATS 2/2")
        self.display.set_actions(action_dict)
        self.display.prompt = "Sélectionnez un vainqueur ou un match nul : "
        choice = self.display.get_input_choice()

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

        self.display.clear()
        self.display.min_character = 0
        self.display.set_title(f"{tournament.name} : RESUME DES TOURS")
        header_list = ["Nom", "Début", "Fin", "Nombre match"]
        self.display.set_content(round_display_list, header_list)
        self.display.set_message(f"Détail du {roud_last.name}")
        header_list = ["Joueur 1", "Joueur 2", "Gagnant"]
        self.display.set_content(match_display, header_list)
        self.display.prompt = "Tapez sur une touche pour continuer."
        return self.display.get_input()


class Tool:

    # Aucun tournoi n'est commencé.
    TOURNAMENT_NOT_STARTING = 0
    # Un tournoi est commencé sans aucun joueur.
    TOURNAMENT_STARTING_WITHOUT_PLAYER = 1
    # Un tournoi et un tour avec des joueurs
    ROUND_STARTING_WITH_PLAYER = 2
    # Un tournoi et un tour sont commencé
    ROUND_STARTING = 3

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

    def get_tournament_statement(self, tournament, round_):
        if tournament is None :
            return self.TOURNAMENT_NOT_STARTING
        elif tournament is not None and round_ is None:
            return self.TOURNAMENT_STARTING
        elif tournament is not None and round_ is not None:
            return self.ROUND_STARTING
        else:
            return None

    def tournament_to_restart(self, tournament_list):
        if len(tournament_list) > 0:
            tournament = tournament_list[-1]
            if self.all_rounf_played(tournament):
                return False
            else:
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

    def all_rounf_played(self, tournament):
        if len(tournament.round_list) >= tournament.DEFAULT_NUMBER_ROUND:
            if not self.round_in_progress:
                return True
            else:
                return False
        else:
            return False

    def get_player_from_id(self, player_list, id_national):
        for player in player_list:
            if player.id_national == id_national:
                return player
        return None