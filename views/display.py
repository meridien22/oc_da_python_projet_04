import os
from tabulate import tabulate

class Display:

    def __init__(self):
        self.title = None
        self.content = None
        self.actions = None
        self.message = None
        self.prompt = None
        self.min_character = 3

    def clear(self):
        os.system('cls')

    def set_title(self, title):
        self.title = title
        print(tabulate([[title]], tablefmt="rounded_outline"))
        print("")

    def set_content(self, content, header_list = None):
        self.content = content
        if header_list is None:
            print(tabulate(self.content, tablefmt="heavy_grid"))
        else:
            print(tabulate(self.content, header_list, tablefmt="heavy_grid"))

    def set_actions(self, actions):
        self.actions = actions
        action_table = []
        for cle in self.actions:
            print(f"[{cle}] {self.actions[cle]}")
            print("")
        print("")
            # action_table.append([cle, self.actions[cle]])
        # print(tabulate(action_table, tablefmt="rounded_grid"))

    def set_message(self, message):
        self.message = message
        print(tabulate([[message]], tablefmt="simple_grid"))

    def set_confirmation(self):
        choice = input(self.prompt)
        if choice in ("y", "Y"):
            return True
        else:
            return False

    def get_input(self):
        while True:
            input_ = input(self.prompt)
            if len(input_) >= self.min_character:
                break
            else:
                print(f"Vous devez au moins saisir {self.min_character} caractères.")
        return input_

    def get_input_choice(self, joker_list = []):
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


class MenuMain(Display):
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
            "11": "Quitter"
        }
        self.clear()
        if tournament is None:
            self.set_title("CHESS MASTER PRO ULTIMATE")
        else:
            self.set_title(str(tournament))
        self.set_actions(actions)
        self.prompt = "Entrez le numéro de votre choix : "
        return self.get_input_choice()


class MenuInscription(Display):
    def execute(self, registration, close, name):
        action_dict = {}
        if registration:
            action_dict["1"] = "Inscrire un joueur"
        if close:
            action_dict["2"] = "Clôturer les inscriptions"
        action_dict["3"] = "Liste des joueurs inscrits"
        action_dict["4"] = "Liste des autres joueurs"
        action_dict["0"] = "Retour au menu principal"
        self.clear()
        self.set_title(f"{name} : MENU INSCRIPTION")
        self.set_actions(action_dict)
        self.prompt = "Entrez le numéro de votre choix : "
        return self.get_input_choice()


class MenuTournament(Display):
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


class MenuNewPlayer(Display):
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


class MenuHint(Display):
    def execute(self, name):
        self.min_character = 1
        self.clear()
        self.set_title(f"{name} : INSCRIPTION - RECHERCHE")
        self.prompt = ("Entrez le nom ou une partie du nom du jouer "
                       "(tapez * pour lister tout les joueurs) : ")

        return self.get_input()


class MenuInscriptionPlayer(Display):
    def execute(self, name, player_list):
        print("")
        action_dict = {}
        # on crée le menu
        number_player_display = 3
        index_start = 0
        index_end = 0
        while index_end <= len(player_list) or isinstance(choice, int):
            index_end = index_start + number_player_display
            list_ = player_list[index_start:index_end]
            for index, player in enumerate(list_):
                action_dict[str(index + 1)] = player
            self.set_actions(action_dict)
            self.prompt = "Entrez le joueur de votre choix (s = suivant, r = retour au début): "
            choice = self.get_input_choice(["s", "r"])
            print(choice)
            os.system("pause")
            if choice == "s":
                index_start += number_player_display
            if choice == "r":
                index_start += 0

        return  int(choice) - 1

class MenuTournamentChoice(Display):
    def execute(self, tournament_list):
        self.clear()
        self.set_title("CHOIX DU TOURNOI A ACTIVER")
        action_dict = {}
        # on crée le menu
        for index, tournament in enumerate(tournament_list):
            action_dict[str(index + 1)] = tournament
        self.set_actions(action_dict)
        self.prompt = "Entrez le joueur de votre choix : "
        choice = self.get_input_choice()

        return  tournament_list[int(choice) - 1]

class MenuPlayerRegister(Display):
    def execute(self, name, player_list):
        self.clear()
        self.min_character = 0
        self.set_title(f"{name} : JOUEURS INSCRITS")
        self.set_content(player_list)
        self.prompt = "Tapez sur une touche pour continuer."
        return self.get_input()


class MenuPlayerOther(Display):
    def execute(self, name, player_list):
        self.clear()
        self.min_character = 0
        self.set_title(f"{name} : JOUEURS DISPONIBLES")
        self.set_content(player_list)
        self.prompt = "Tapez sur entrée pour continuer."
        return self.get_input()


class MenuPlayerFull(Display):
    def execute(self, name, player_list):
        self.clear()
        self.min_character = 0
        self.set_title("LISTE DE TOUS LES JOUEURS")
        self.set_content(player_list)
        self.prompt = "Tapez sur entrée pour continuer."
        return self.get_input()


class MenuTournamentFull(Display):
    def execute(self, tournament_list):
        self.clear()
        self.min_character = 0
        self.set_title(f"LISTE DE TOUS LES TOURNOIS")
        header_list = ["Nom du tournoi", "Emplacement", "Nombre de round", "Nombre de joueur"]
        self.set_content(tournament_list, header_list)
        self.prompt = "Tapez sur entrée pour continuer."
        return self.get_input()


class MenuRound(Display):
    def execute(self, tournament_name, round_name):
        actions = {
            "1": "Saisir les résultats",
            "2": "Résumé des tours",
            "0": "Retour au menu principal"
        }
        self.clear()
        self.set_title(f"{tournament_name} {round_name}")
        self.set_actions(actions)
        self.prompt = "Entrez le numéro de votre choix : "
        return self.get_input_choice()

class MenuEnterResult(Display):
    def execute(self, action_dict, tournament_name, round_name):
        self.clear()
        self.set_title(f"{tournament_name} - {round_name} - SAISIE DES RESULTATS 1/2")
        self.set_actions(action_dict)
        self.prompt = "Sélectionnez un match à encoder : "
        choice = self.get_input_choice()

        return  int(choice) - 1

class MenuEnterMacthResult(Display):
    def execute(self, action_dict, tournament_name, round_name):
        self.clear()
        self.set_title(f"{tournament_name} - {round_name} - SAISIE DES RESULTATS 2/2")
        self.set_actions(action_dict)
        self.prompt = "Sélectionnez un vainqueur ou un match nul : "
        choice = self.get_input_choice()

        return choice


class MenuRoundREsume(Display):
    def execute(self, tournament_name, round_name, round_list, match_list):
        self.clear()
        self.min_character = 0
        self.set_title(f"{tournament_name} : RESUME DES TOURS")
        header_list = ["Nom", "Début", "Fin", "Nombre match"]
        self.set_content(round_list, header_list)
        self.set_message(f"Détail du {round_name}")
        header_list = ["Joueur 1", "Joueur 2", "Gagnant"]
        self.set_content(match_list, header_list)
        self.prompt = "Tapez sur entrée pour continuer."

        return self.get_input()

class InformationUser(Display):
    def execute(self, code):
        self.clear()
        message = ""
        match code:
            case 1:
                message = ("Vous devez créer au moins un tournoi \n"
                           "avant de pouvoir en activer.")
            case 2:
                message = "Vous devez d'abord activer un tournoi."
            case 3:
                message = "Les inscriptions sont closes pour ce tournoi."
            case 4:
                message = "Il n'y a plus de joueur disponible pour l'inscription"
        self.set_message(message)
        os.system("pause")