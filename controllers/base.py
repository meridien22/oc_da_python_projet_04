import random
import datetime
import re
from views import *

class Controller:
    def __init__(self, display):
        self.display = display

    def get_main_menu(self):
        self.display.configure(display_parameters["00"])
        return self.display.get_input_choice()

    def get_main_menu_tournament(self):
        self.display.configure(display_parameters["001"])
        return self.display.get_input_choice()

    def get_input_tournament_name(self):
        self.display.configure(display_parameters["10"])
        return self.display.get_input()

    def get_input_tournament_place(self):
        self.display.configure(display_parameters["11"])
        return self.display.get_input()

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

    def get_input_player_name(self):
        self.display.configure(display_parameters["30"])
        return self.display.get_input()

    def get_input_player_hint(self):
        self.display.configure(display_parameters["40"])
        return self.display.get_input()

    def get_confirmation(self):
        self.display.configure(display_parameters["50"])
        return self.display.get_input()

    def get_list_round_match(self, tournament_active):
        parameter = display_parameters["100"]
        parameter["content"] = tournament_active.get_rounds_matchs()
        self.display.configure(parameter)
        return self.display.get_input()

class Tool():
    def set_main_tile(self, title):
        title = f"Tournoi en cours : {title}"
        display_parameters["001"]["title"] = title

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
