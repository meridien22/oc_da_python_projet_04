import os
from abc import ABC, abstractmethod
from tabulate import tabulate

class Command(ABC):
    # L'interface Command déclare une méthode pour exécuter une commande.
    @abstractmethod
    def execute(self) -> None:
        pass

class Invocateur:
    _on_start = None
    _build_title = None
    _build_content = None
    _build_actions = None
    _build_input = None
    _buid_message = None
    _on_finish = []

class EffacerTerminal(Command):
    def execute(self):
        os.system('cls')


class AfficherTitre(Command):

    def __init__(self, titre):
        self._titre = titre

    def execute(self):
        print(tabulate([[self._titre]], tablefmt="rounded_outline"))


class AfficherActions(Command):

    def __init__(self, actioneur):
        self._actioneur = actioneur

    def execute(self):
        print(tabulate(self._actioneur.get_affichage_actions(),tablefmt="rounded_grid"))

class AfficherTournoisCommand(Command):
    """
    Commande qui permet de charger le fichier JSON avec les données des tournois.
    """

    def __init__(self, actioneur):
        self._actioneur= actioneur

    def execute(self) -> None:
        # Les commandes peuvent être déléguées à n’importe quelle méthode d’un récepteur.
        self._actioneur.charger_tournoi()