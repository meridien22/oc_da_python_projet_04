import os
from .tableau import Tableau

class TerminalView:

    def __init__(self):
        self.tableau = Tableau()

    def afficher_menu(self, menu_base):
        os.system('cls')
        self.tableau.afficher_titre(menu_base.titre)
        self.tableau.afficher_actions(menu_base.actions)

        while True:
            try:
                choix = int(input("Entrez votre choix :"))
                if 1 <= choix <= len(self.menus):
                    break
                else:
                    self.afficher("Choix invalide. Veuillez entrer un numéro de la liste.")
                    break
            except ValueError:
                self.afficher("Choix invalide. Veuillez entrer un numéro de la liste.")
                break