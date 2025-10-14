from controllers import ManagerTool
from models import Tournament, Player
from views import MenuConfirmation, MenuTournament, MenuNewPlayer


class ManagerText:
    def __init__(self, display):
        self.manager_tool = ManagerTool()

    def get_confirmation(self, message):
        """Demande à l'utilisateur de confirmer et renvoi True ou False"""
        menu = MenuConfirmation()
        return menu.execute(message)

    def get_tournament(self):
        """Renvoi un nouveau tournoi"""
        menu = MenuTournament()
        value_dict = menu.execute()
        return Tournament(value_dict["name"],
                          value_dict["location"],
                          None,
                          value_dict["description"],
                          value_dict["number_round"])

    def get_new_player(self):
        """Renvoi un nouveau joueur"""
        player_id_national = self.manager_tool.get_national_id()
        menu = MenuNewPlayer()
        value_dict = menu.execute()
        return Player(value_dict["name"],
                      value_dict["fist_name"],
                      value_dict["date_birth"],
                      player_id_national)
