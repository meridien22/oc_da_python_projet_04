from email._header_value_parser import Terminal

from models import *
from controllers import *
from views import *

from data.donnees_test import joueurs_test
from data.donnees_test import tournoi_test
from views.terminal import TerminalView


def lancer_tournoi_auto():
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
    print(tournoi.get_score())

def lancer_tournoi_manuel():
    # choix = [
    #     [1,"Saisir un nouveau tournoi", Command],
    #     [2,"Charger un tournoi"]
    # ]
    # titre = "Menu principal"
    # menu = TerminalView(titre, choix)
    # menu.afficher_menus()
    manager = TournoiManager()
    afficher_tournoi= AfficherTournoisCommand(manager)
    menu_base = Menu("Gestion des tournois")
    menu_base.ajouter_action("Consulter tout les tournois", afficher_tournoi)
    terminal = TerminalView()
    terminal.afficher_menu(menu_base)



lancer_tournoi_auto()
# lancer_tournoi_manuel()