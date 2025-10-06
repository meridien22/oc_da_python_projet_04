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
            action_table.append([cle, self.actions[cle]])
        print(tabulate(action_table, tablefmt="rounded_grid"))

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

    def get_input_choice(self):
        choice_possible = []
        for cle in self.actions:
            choice_possible.append(cle)

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


