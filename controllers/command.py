from __future__ import annotations
from abc import ABC, abstractmethod

class Command(ABC):
    # L'interface Command déclare une méthode pour exécuter une commande.
    @abstractmethod
    def execute(self) -> None:
        pass


class AfficherTournoisCommand(Command):
    """
    Commande qui permet de charger le fichier JSON avec les données des tournois.
    """

    def __init__(self, actioneur):
        self._actioneur= actioneur

    def execute(self) -> None:
        # Les commandes peuvent être déléguées à n’importe quelle méthode d’un récepteur.
        self._actioneur.charger_tournoi()