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
        tournoi.ajouter_joueur_score(joueur)

    print("--------------------------------------------------------")
    print(tournoi)
    print("--------------------------------------------------------")

    compteur_tour = 1
    while compteur_tour <= tournoi.nombre_tour:
        tour = Tour(tournoi, "Round " + str(compteur_tour))
        print(tour)
        if compteur_tour == 1:
            tour.melanger_joueur()
        else:
            tour.trier_joueur()
        print(tournoi.get_score())
        tour.generer_match()
        print(tour.get_match_resume())
        tour.auto_play()
        tour.finir()
        compteur_tour += 1

main()