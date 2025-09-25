import datetime
import random
from .match import Match

class Tour:
    """Créer un tour pour un tournoi d'échec"""
    def __init__(self, tournoi, nom):
        self.nom = nom
        self.date_heure_debut = self.get_date_heure()
        self.tournoi = tournoi
        self.matchs = []

    def __str__(self):
        return (f"Tour {self.nom } du tournoi {self.tournoi.nom} "
                f"{len(self.matchs)} matchs")

    def get_date_heure(self):
        """Retourne la date du jour avec les heures et les minutes"""
        return datetime.datetime.now().strftime("%d/%m/%Y à %Hh%M")

    def melanger_joueur(self):
        """Mélange les joueurs d'un tour de manière aléatoire"""
        random.shuffle(self.tournoi.joueurs)

    def generer_match(self):
        """Retourne la liste des matchs d'un tour"""
        index_joueur_1 = 0
        index_joueur_2 = 1

        while index_joueur_2 < len(self.tournoi.joueurs):
            joueur_1 = self.tournoi.joueurs[index_joueur_1]
            joueur_2 = self.tournoi.joueurs[index_joueur_2]
            match = Match(self.tournoi, self, joueur_1, joueur_2)
            self.matchs.append(match)
            index_joueur_1 += 2
            index_joueur_2 += 2

    def generer_match_old(self):
        """Retourne la liste des matchs d'un tour d'un tournoi"""
        identifiant_matchs = []
        for joueur1 in self.tournoi.joueurs:
            for joueur2 in self.tournoi.joueurs:
                if joueur1 != joueur2:
                    match = Match(self.tournoi, self, joueur1, joueur2)
                    if match.identifiant not in identifiant_matchs:
                        self.matchs.append(match)
                        identifiant_matchs.append(match.identifiant)

    def get_resultat(self):
        """Donne les scores des joueurs pour le tour"""
        resultats = []
        for match in self.matchs:
            joueur_1 = match.get_joueur_1()
            joueur_2 = match.get_joueur_2()
            score_1 = match.get_score_joueur_1()
            score_2 = match.get_score_joueur_2()
            resultats.append(f"{joueur_1} : {score_1}")
            resultats.append(f"{joueur_2} : {score_2}")
        return resultats