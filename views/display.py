import os
from tabulate import tabulate


class Display:

    def __init__(self):
        self.title = None
        self.content = None
        self.actions = None
        self.message = None
        self.input = None
        self.input_choice = None
        self.parameters = None

    def configure(self, parameter):
        self.title = parameter["title"]
        self.content = parameter["content"]
        self.actions = parameter["actions"]
        self.input = parameter["input"]
        self.input_choice = parameter["input_choice"]

    def initialize(self):
        os.system('cls')
        self.set_title()
        self.set_content()
        self.set_actions()

    def get_input(self):
        self.initialize()
        while True:
            choice = input(self.input)
            if len(choice) >=3:
                break
            else:
                print("Vous devez au moins saisir 3 caractères.")
        return choice

    def get_confirmation(self):
        self.initialize()
        choice = input(self.input)
        if choice in ("y", "Y"):
            return True
        else:
            return False

    def get_input_choice(self):
        self.initialize()

        choice_possible = []
        for cle in self.actions:
            choice_possible.append(cle)

        while True:
            try:
                choice = input(self.input_choice)
                if choice in choice_possible:
                    break
                else:
                    print("Choix invalide. Veuillez entrer un numéro de la liste.")
            except ValueError:
                print("Saisie invalide. Veuillez entrer un nombre.")
        return choice

    def set_title(self):
        print(tabulate([[self.title]], tablefmt="rounded_outline"))

    def set_content(self):
        if self.content is not None:
            print(tabulate([self.content], tablefmt="rounded_outline"))

    def set_actions(self):
            if self.actions is not None:
                action_table = []
                for cle in self.actions:
                    action_table.append([cle, self.actions[cle]])
                print(tabulate(action_table, tablefmt="rounded_grid"))
