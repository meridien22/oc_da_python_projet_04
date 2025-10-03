import random
import datetime
import re
from views import *

class Controller:
    def __init__(self, display):
        self.display = display

    def get_menu_choice(self, id_menu):
        self.display.configure(display_parameters[id_menu])
        return self.display.get_input_choice()

    def get_menu_input(self, id_menu):
        self.display.configure(display_parameters[id_menu])
        return self.display.get_input()

    def get_confirmation(self):
        self.display.configure(display_parameters["50"])
        return self.display.get_confirmation()

    def get_list_tournament(self, tournament_liste):
        parameter = display_parameters["20"]
        action_dict = {}

        for index, tournament in enumerate(tournament_liste):
            action_dict[str(index + 1)] = tournament.name

        parameter["actions"] = action_dict
        self.display.configure(parameter)
        return self.display.get_input_choice()

    def get_list_player(self, player_list_hint, player_list_all):
        parameter = display_parameters["41"]
        action_dict = {}

        for index, player in enumerate(player_list_all):
            if player in player_list_hint:
                action_dict[str(index + 1)] = player.name

        parameter["actions"] = action_dict
        self.display.configure(parameter)
        return self.display.get_input_choice()

    def get_list_round_match(self, tournament_active):
        parameter = display_parameters["100"]
        parameter["content"] = tournament_active.get_rounds_matchs()
        self.display.configure(parameter)
        return self.display.get_input()

class Tool():

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