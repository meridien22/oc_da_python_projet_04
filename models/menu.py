class Menu:

    def __init__(self):
        # Construit un menu avec un titre.
        self.actions = []

    def ajouter_action(self, libelle, command):
        # Ajoute une action au menu à partir d'un libelle et d'une commande.
        index = len(self.actions) + 1
        self.actions.append([index, libelle, command])

    def get_affichage_actions(self):
        affichage = []
        for action  in self.actions:
            affichage.append([action[0], action[1]])
        return affichage
