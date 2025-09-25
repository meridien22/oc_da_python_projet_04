from models.joueur import Joueur
from models.tournoi import Tournoi
from models.tour import Tour
from models.match import Match
from data.donnees_test import joueurs_test
from data.donnees_test import tournoi_test

def main():
    tournoi = Tournoi(tournoi_test[0], tournoi_test[1], tournoi_test[2], tournoi_test[3], tournoi_test[4])
    for joueur in joueurs_test:
        joueur = Joueur(joueur[0], joueur[1], joueur[2], joueur[3])
        tournoi.ajouter_joueur(joueur)
    print(tournoi)
    tour = Tour(tournoi, "Round 1")
    tour.melanger_joueur()
    tour.generer_match()
    print(tour)
    for match in tour.matchs:
        print(match)
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
    print(tour.get_resultat())
main()