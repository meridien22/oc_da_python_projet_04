import json
import os

class TournoiManager():
    """
    Classe qui permet de gérer un ensemble de tournoi d'échec.
    """

    # emplacement où sont stockées les données
    JSON_DIRECTORY = "data"
    # nom du fichier json où sont stockés les données
    JSON_FILE = "tournois.json"

    def __init__(self):
        self.tournois = []
        self.data = {}
        self.charger_tournoi()

    def charger_tournoi(self):
        with open(os.path.join(self.JSON_DIRECTORY, self.JSON_FILE), 'r', encoding='utf-8') as fichier:
            self.data = json.load(fichier)