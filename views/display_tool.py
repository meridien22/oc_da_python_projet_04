import os
from tabulate import tabulate


class DisplayTool:
    """Permet gérer un affichage d'une page dans un terminal"""
    def __init__(self):
        self.title = None
        self.content = None
        self.actions = None
        self.message = None
        self.prompt = None
        self.min_character = 3

    def clear(self):
        """"Vide la console"""
        os.system('cls')

    def set_title(self, title):
        """Affiche le titre de la page"""
        self.title = title
        print(tabulate([[title]], tablefmt="rounded_outline"))
        print("")

    def set_content(self, content, header_list=None):
        """Afficher un contenu sous forme de tableau
        Accepte un paramètre facultatif contenant les en-têtes du tableau"""
        self.content = content
        if header_list is None:
            print(tabulate(self.content, tablefmt="heavy_grid"))
        else:
            print(tabulate(self.content, header_list, tablefmt="heavy_grid"))

    def set_actions(self, actions):
        """Affiche une liste de choix à l'utilisateur"""
        self.actions = actions
        for cle in self.actions:
            print(f"[{cle}] {self.actions[cle]}")
            print("")
        print("")

    def set_message(self, message):
        """Affiche un message d'information à l'utilisateur"""
        self.message = message
        print(tabulate([[message]], tablefmt="simple_grid"))

    def get_confirmation(self):
        """Affiche un message demandant à l'utilisateur une confirmation"""
        choice = input(self.prompt)
        if choice in ("y", "Y"):
            return True
        else:
            return False

    def get_input(self):
        """Demande à l'utilsateur de saisir un texte"""
        while True:
            input_ = input(self.prompt)
            if len(input_) >= self.min_character:
                break
            else:
                print(f"Vous devez au moins saisir {self.min_character} caractères.")
        return input_

    def get_input_choice(self, joker_list=[]):
        """Demande à l'utilisateur de choisir parmi des propositions"""
        choice_possible = []
        for cle in self.actions:
            choice_possible.append(cle)

        for joker in joker_list:
            choice_possible.append(joker)

        while True:
            try:
                choice = input(self.prompt)
                if choice in choice_possible:
                    break
                else:
                    print("Choix invalide. Veuillez entrer un numéro de la liste.")
            except ValueError:
                print("Saisie invalide. Veuillez entrer un nombre.")
        return choice


class InformationUser(DisplayTool):
    """Lance l'affichage d'un message avec un contenu précis"""
    def execute(self, code, parameter=None):
        self.clear()
        self.set_title("MESSAGE D'INFORMATION")
        self.set_message(self.get_message(code, parameter))
        print("")
        os.system("pause")

    @staticmethod
    def get_message(code, parameter=None):
        """Faire correspondre un message à un code"""
        message_dict = {
            "1": "Vous devez créer au moins un tournoi avant de pouvoir en activer.",
            "2": "Vous devez d'abord activer un tournoi.",
            "3": "Les inscriptions sont closes pour ce tournoi.",
            "4": "Il n'y a plus de joueur disponible pour l'inscription.",
            "5": "Vous devez d'abord finir le tour en cours avant d'en commencer un nouveau.",
            "6": (f"Le tournoi comporte déjà {parameter} tours ce qui est le nombre "
                  f"de tour total du tournoi."),
            "7": "Il n'y a pas assez de joueurs disponible pour commencer l'inscription",
            "8": "La création du premier tour va clôturer définitivement les inscriptions.",
            "9": "Veuillez inscrire plus de joueur au tournoi pour le débuter.",
            "10": "Il n'y a aucun joueur inscrit dans ce tournoi.",
            "11": "Il n'est plus possible d'inscrire des jouers dans ce tournoi.",
            "12": "Ce tournoi ce comporte pas encore de tour.",
            "13": "Il n'y a aucun résultat à saisir dans ce tournoi.",
            "14": "Le tournoi est terminé, vous pouvez consulter le classement.",
            "15": "Vous devez inscrire un joueur supplémentaire avent de démmarrer le tournoi.",
            "16": "Le tour est maintenant terminé."
        }
        return message_dict[code]
