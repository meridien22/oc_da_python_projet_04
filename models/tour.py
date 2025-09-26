import datetime
import random
from .match import Match

class Tour:
    """Créer un tour pour un tournoi d'échec"""
    def __init__(self, tournoi, nom):
        self.nom = nom
        self.date_heure_debut = self.get_date_heure()
        self.date_heure_fin = None
        self.tournoi = tournoi
        self.matchs = []

    def __str__(self):
        return (f"Tour {self.nom}")

    def get_date_heure(self):
        """Retourne la date du jour avec les heures et les minutes"""
        return datetime.datetime.now().strftime("%d/%m/%Y à %Hh%M")

    def melanger_joueur(self):
        """Mélange les joueurs d'un tour de manière aléatoire"""
        random.shuffle(self.tournoi.joueurs_scores)

    def trier_joueur(self):
        """Trie les joueurs en fonction de leur score"""
        self.tournoi.joueurs_scores.sort(key=lambda element:element[1])

    def generer_match(self):
        """Retourne la liste des matchs d'un tour"""
        index_joueur_score_1 = 0
        index_joueur_score_2 = 1

        while index_joueur_score_2 < len(self.tournoi.joueurs_scores):
            joueur_score_1 = self.tournoi.joueurs_scores[index_joueur_score_1]
            joueur_score_2 = self.tournoi.joueurs_scores[index_joueur_score_2]
            match = Match(self.tournoi, self, joueur_score_1, joueur_score_2)
            if match.identifiant not in self.tournoi.identifiant_matchs:
                self.matchs.append(match)
                self.tournoi.identifiant_matchs.append(match.identifiant)
            else:
                self.eviter_rejouer_match(index_joueur_score_2)
                joueur_score_1 = self.tournoi.joueurs_scores[index_joueur_score_1]
                joueur_score_2 = self.tournoi.joueurs_scores[index_joueur_score_2]
                match = Match(self.tournoi, self, joueur_score_1, joueur_score_2)
                self.matchs.append(match)
                self.tournoi.identifiant_matchs.append(match.identifiant)
            index_joueur_score_1 += 2
            index_joueur_score_2 += 2

    def eviter_rejouer_match(self, index_joueur_score_2):
        """En cas de match déjà joué, permet de proposer un match
        entre leindex_joueur_score_2 joueur 1 et le joueur situé après le joueur 2"""
        if index_joueur_score_2 < len(self.tournoi.joueurs_scores) - 1:
            joueur_score = self.tournoi.joueurs_scores.pop(index_joueur_score_2)
            self.tournoi.joueurs_scores.insert(index_joueur_score_2 + 1, joueur_score)

    def get_match_resume(self):
        """Retourne la liste des matchs d'un tour"""
        match_resume = []
        for match in self.matchs:
            match_resume.append(str(match))
        return " / ".join(match_resume)

    def auto_play(self):
        """Simule un tour en résolvant aléatoirement les matchs"""
        for match in self.matchs:
            gagnant = match.get_gagnant_aleatoire()
            if gagnant:
                perdant = match.get_autre_joueur(gagnant)
                match.ajouter_score(gagnant, Match.SCORE_GAGNANT)
                match.ajouter_score(perdant, Match.SCORE_PERDANT)
            else:
                joueur_1 = match.get_joueur_1()
                joueur_2 = match.get_joueur_2()
                match.ajouter_score(joueur_1, Match.SCORE_MATCH_NUL)
                match.ajouter_score(joueur_2, Match.SCORE_MATCH_NUL)

    def finir(self):
        self.date_heure_fin = self.get_date_heure()