import datetime
import random
from .match import Match

class Round:
    """Créer un tour pour un tournoi d'échec"""
    def __init__(self, match_list):
        self.name = None
        self.date_time_start = self.get_date_time()
        self.date_time_end = None
        self.match_list = match_list

    def __str__(self):
        return (f"Tour {self.name}")

    def get_date_time(self):
        """Retourne la date du jour avec les heures et les minutes"""
        return datetime.datetime.now().strftime("%d/%m/%Y à %Hh%M")

    def sort_joueur(self):
        """Trie les joueurs en fonction de leur score"""
        # self.tournoi.joueurs_scores.sort(key=lambda element:element[1])
        print("fonction à implémenter")

    def generer_match(self):
        """Retourne la liste des matchs d'un tour"""
        print("fonction à implémenter")
        # index_joueur_score_1 = 0
        # index_joueur_score_2 = 1
        #
        # while index_joueur_score_2 < len(self.tournoi.joueurs_scores):
        #     joueur_score_1 = self.tournoi.joueurs_scores[index_joueur_score_1]
        #     joueur_score_2 = self.tournoi.joueurs_scores[index_joueur_score_2]
        #     match = Match(self.tournoi, self, joueur_score_1, joueur_score_2)
        #     if match.identifiant not in self.tournoi.identifiant_matchs:
        #         self.matchs.append(match)
        #         self.tournoi.identifiant_matchs.append(match.identifiant)
        #     else:
        #         self.eviter_rejouer_match(index_joueur_score_2)
        #         joueur_score_1 = self.tournoi.joueurs_scores[index_joueur_score_1]
        #         joueur_score_2 = self.tournoi.joueurs_scores[index_joueur_score_2]
        #         match = Match(self.tournoi, self, joueur_score_1, joueur_score_2)
        #         self.matchs.append(match)
        #         self.tournoi.identifiant_matchs.append(match.identifiant)
        #     index_joueur_score_1 += 2
        #     index_joueur_score_2 += 2

    def eviter_rejouer_match(self, index_joueur_score_2):
        """En cas de match déjà joué, permet de proposer un match
        entre leindex_joueur_score_2 joueur 1 et le joueur situé après le joueur 2"""
        print("fonction à implémenter")
        # if index_joueur_score_2 < len(self.tournoi.joueurs_scores) - 1:
        #     joueur_score = self.tournoi.joueurs_scores.pop(index_joueur_score_2)
        #     self.tournoi.joueurs_scores.insert(index_joueur_score_2 + 1, joueur_score)

    def get_match_resume(self):
        """Retourne la liste des matchs d'un tour"""
        match_list = []
        for match in self.match_list:
            match_list.append(str(match))
        return match_list

    def auto_play(self):
        """Simule un tour en résolvant aléatoirement les matchs"""
        for match in self.match_list:
            match.winner = match.get_winner()

    def finir(self):
        print("fonction à implémenter")
        # self.date_heure_fin = self.get_date_heure()