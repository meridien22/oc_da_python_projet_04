from views.display_text import *
from models import *


class MangerText:

    def get_confirmation(self, message):
        """Demande à l'utilisateur de confirmer et renvoi True ou False"""
        menu = MenuConfirmation()
        return menu.execute(message)

    def get_tournament(self):
        """Renvoi un nouveau tournoi"""
        tournament_id = self.tool.get_national_id()
        menu = MenuTournament()
        value_dict = menu.execute()
        return Tournament(tournament_id,
                          value_dict["name"],
                          value_dict["location"],
                          "", "")

    def get_new_player(self):
        """Renvoi un nouveau joueur"""
        player_id_national = self.tool.get_national_id()
        menu = MenuNewPlayer()
        value_dict = menu.execute()
        return Player(value_dict["name"], value_dict["fist_name"], "", player_id_national)