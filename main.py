from models import *

# def lancer_tournoi_auto():
#     tournoi = Tournoi(tournoi_test[0], tournoi_test[1], tournoi_test[2], tournoi_test[3], tournoi_test[4])
#     for joueur in joueurs_test :
#         joueur = Joueur(joueur[0], joueur[1], joueur[2], joueur[3])
#         tournoi.ajouter_joueur_score(joueur)
#
#     print("--------------------------------------------------------")
#     print(tournoi)
#     print("--------------------------------------------------------")
#
#     compteur_tour = 1
#     while compteur_tour <= tournoi.nombre_tour:
#         tour = Tour(tournoi, "Round " + str(compteur_tour))
#         print(tour)
#         if compteur_tour == 1:
#             tour.melanger_joueur()
#         else:
#             tour.trier_joueur()
#         print(tournoi.get_score())
#         tour.generer_match()
#         print(tour.get_match_resume())
#         tour.auto_play()
#         tour.finir()
#         compteur_tour += 1
#     print(tournoi.get_score())
#     pass

# def lancer_tournoi_manuel():
    # choix = [
    #     [1,"Saisir un nouveau tournoi", Command],
    #     [2,"Charger un tournoi"]
    # ]
    # titre = "Menu principal"
    # menu = TerminalView(titre, choix)
    # menu.afficher_menus()
    # manager = TournoiManager()
    # afficher_tournoi= AfficherTournoisCommand(manager)
    # menu_base = Menu("Gestion des tournois")
    # menu_base.ajouter_action("Consulter tout les tournois", afficher_tournoi)
    # terminal = TerminalView()
    # terminal.afficher_menu(menu_base)




# lancer_tournoi_auto()
# lancer_tournoi_manuel()

player_1 = Player("Lazu", "Cynel", "1/11/1982", "IB12345")
player_2 = Player("Poular", "Rose", "1/12/1815", "JB12345")
player_3 = Player("Kasparov", "Garry", "13/04/1963", "AA00000")
player_4 = Player("Blue", "Deep", "15/05/1997", "XX00000")
player_5 = Player("Godin", "André", "1/03/2003", "EB12345")
player_6 = Player("Gardies", "Ludivine", "1/05/2004", "FB12345")
player_7 = Player("Guillot", "Rodrigue", "1/07/1980", "GB12345")
player_8 = Player("Calabre", "Antoine", "1/10/1970", "HB12345")

# Le tournoi est créé.
tournament = Tournament("T01", "Le Grand échiquier", "Libreville", "01/12/2025", "")
# Des joueurs s'incrivent au tournoi.
tournament.add_player(player_1)
tournament.add_player(player_2)
tournament.add_player(player_3)
tournament.add_player(player_4)
tournament.add_player(player_5)
tournament.add_player(player_6)
tournament.add_player(player_7)
tournament.add_player(player_8)

print("")
# Le tournoi génère les premiers matchs du premier tour et crée le premier tour.
round_ = Round(tournament.get_match())
# Le tour est joué.
round_.auto_play()
print(round_.get_match_resume())
tournament.add_round(round_)
print(tournament.get_score())

print("")
# Le tournoi génère les matchs du tour suivant et crée le tour.
round_ = Round(tournament.get_match())
# Le tour est joué.
round_.auto_play()
print(round_.get_match_resume())
tournament.add_round(round_)
print(tournament.get_score())

print("")
# Le tournoi génère les matchs du tour suivant et crée le tour.
round_ = Round(tournament.get_match())
# Le tour est joué.
round_.auto_play()
print(round_.get_match_resume())
tournament.add_round(round_)
print(tournament.get_score())

print("")
# Le tournoi génère les matchs du tour suivant et crée le tour.
round_ = Round(tournament.get_match())
# Le tour est joué.
round_.auto_play()
print(round_.get_match_resume())
tournament.add_round(round_)
print(tournament.get_score())





