from .display_tool import *


class MenuTournament(DisplayTool):
    """Renvoi les informations nécessaires à la création d'un tournoi"""
    def execute(self):
        self.min_character = 3
        self.clear()
        self.set_title("CREATION D'UN TOURNOI")
        self.prompt = "Entrez le nom du tournoi : "
        name = self.get_input()
        print("")
        self.prompt = "Entrez le lieu du tournoi : "
        location = self.get_input()

        return {"name": name, "location": location}


class MenuNewPlayer(DisplayTool):
    """Renvoi les informations nécessaire à la création d'un joueur"""
    def execute(self):
        self.min_character = 3
        self.clear()

        self.set_title("CREATION D'UN JOUEUR")
        self.prompt = "Entrez le prénom du joueur : "
        first_name = self.get_input()
        print("")
        self.prompt = "Entrez le nom du joueur : "
        name = self.get_input()

        return {"name": name, "fist_name": first_name}


class MenuHint(DisplayTool):
    """Renvoi le critère de recherche saisi par l'utilisateur"""
    def execute(self, name):
        self.min_character = 1
        self.clear()
        self.set_title(f"{name} : INSCRIPTION D'UN JOUEUR")
        self.prompt = ("Entrez le nom ou une partie du nom du jouer "
                       "(tapez * pour lister tout les joueurs) : ")

        return self.get_input()

class MenuConfirmation(DisplayTool):
    """Demande à l'utilisateur de confirmer et renvoi True ou False"""
    def execute(self, message):
        self.clear()
        self.set_title("DEMANDE DE CONFIRMATION")
        self.set_message(message)
        self.prompt = "Tapez Y ou y pour confirmer."
        return self.get_confirmation()