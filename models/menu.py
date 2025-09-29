class Menu:

    def __init__(self, titre):
        # Construit un menu avec un titre.
        self.titre = titre
        self.actions = []

    def ajouter_action(self, libelle, command):
        # Ajoute une action au menu à partir d'un libelle et d'une commande.
        index = len(self.actions) + 1
        self.actions.append([index, libelle, command])