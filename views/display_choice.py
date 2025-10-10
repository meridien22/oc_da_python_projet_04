from .display_tool import *


class MenuMain(DisplayTool):
    """Renvoi le choix de l'utilisateur dans le menu principal"""
    def execute(self, tournament):
        actions = {
            "1": "Créer un tournoi",
            "2": "Saisir un nouveau joueur",
            "3": "Activer un tournoi",
            "4": "Inscrire un joueur",
            "5": "Démarrer un tour",
            "6": "Saisir des résultats",
            "7": "Résumé des tours",
            "8": "Liste des joueus inscrits",
            "9": "Liste tous les joueurs",
            "10": "Lister tous les tournois",
            "11": "Classement du tournoi",
            "12": "Quitter"
        }
        self.clear()
        if tournament is None:
            self.set_title("CHESS MASTER PRO ULTIMATE")
        else:
            self.set_title(str(tournament))
        self.set_actions(actions)
        self.prompt = "Entrez le numéro de votre choix : "
        return self.get_input_choice()


class MenuListPaginated(DisplayTool):
    """Renvoi la commande saisi par l'utilisateur pour naviguer dans des pages"""
    def execute(self, title, header_list, list_, page, page_full):
        self.clear()
        self.set_title(title)
        self.set_content(list_, header_list)
        self.actions = []
        self.prompt = (f"[s = suivant] "
                       f"[r = début] "
                       f"[a = annuler] "
                       f"[Page {page}/{page_full}] :")

        return  self.get_input_choice(['s', 'r', 'a'])


class MenuInscriptionPlayer(DisplayTool):
    """Renvoi la commande saisi par l'utilisateur pour naviguer la liste des jouers
    Permet également de choisir un joueur dans la page"""
    def execute(self, name, player_dict, page, page_full):
        self.clear()
        self.set_title(f"{name} : INSCRIPTION D'UN JOUEUR")
        action_dict = {}
        # on crée le menu
        for key, value in player_dict.items():
            action_dict[str(int(key) + 1)] = value
        self.set_actions(action_dict)
        self.prompt = (f"[Selectionnez un joueur] "
                       f"[s = suivant] "
                       f"[r = début] "
                       f"[a = annuler] "
                       f"[Page {page}/{page_full}] :")

        return  self.get_input_choice(['s', 'r', 'a'])


class MenuTournamentChoice(DisplayTool):
    """Renvoi le tournoi sélectionné parmi une liste de tournoi"""
    def execute(self, tournament_list):
        self.clear()
        self.set_title("CHOIX DU TOURNOI A ACTIVER")
        action_dict = {}
        # on crée le menu
        for index, tournament in enumerate(tournament_list):
            action_dict[str(index + 1)] = tournament
        self.set_actions(action_dict)
        self.prompt = "Entrez le joueur de votre choix : "

        return  self.get_input_choice()


class MenuEnterResult(DisplayTool):
    """Propose à l'utilisateur une liste de match à encoder"""
    def execute(self, action_dict, tournament_name, round_name):
        self.clear()
        self.set_title(f"{tournament_name} - {round_name} - SAISIE DES RESULTATS 1/2")
        self.set_actions(action_dict)
        self.prompt = "Sélectionnez un match à encoder : "

        return  self.get_input_choice()


class MenuEnterMacthResult(DisplayTool):
    """Permet à l'utilisateur d'indiquer le résultat d'un match"""
    def execute(self, action_dict, tournament_name, round_name):
        self.clear()
        self.set_title(f"{tournament_name} - {round_name} - SAISIE DES RESULTATS 2/2")
        self.set_actions(action_dict)
        self.prompt = "Sélectionnez un vainqueur ou un match nul : "

        return self.get_input_choice()
