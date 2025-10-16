import os
from views import DisplayTool


class MenuPlayerList(DisplayTool):
    """Affiche une liste de joueur"""
    def execute(self, name, player_list):
        self.clear()
        self.min_character = 0
        self.set_title(f"{name} : JOUEURS INSCRITS")
        self.set_content(player_list)
        print("")
        os.system("pause")


class MenuRoundResume(DisplayTool):
    """Affiche le résumé des tours"""
    def execute(self, tournament_name, round_name, round_list, match_list, pause=True):
        self.clear()
        self.min_character = 0
        self.set_title(f"{tournament_name} : RESUME DES TOURS")
        header_list = ["Nom", "Début", "Fin", "Nombre match"]
        self.set_content(round_list, header_list)
        self.set_message(f"Détail du {round_name}")
        header_list = ["Joueur 1", "Joueur 2", "Gagnant"]
        self.set_content(match_list, header_list)
        print("")
        if pause:
            os.system("pause")
