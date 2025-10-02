import os
from controllers import *
from models import *
from views import *

# player_1 = Player("Lazu", "Cynel", "1/11/1982", "IB12345")
# player_2 = Player("Poular", "Rose", "1/12/1815", "JB12345")
# player_3 = Player("Kasparov", "Garry", "13/04/1963", "AA00000")
# player_4 = Player("Blue", "Deep", "15/05/1997", "XX00000")
# player_5 = Player("Godin", "André", "1/03/2003", "EB12345")
# player_6 = Player("Gardies", "Ludivine", "1/05/2004", "FB12345")
# player_7 = Player("Guillot", "Rodrigue", "1/07/1980", "GB12345")
# player_8 = Player("Calabre", "Antoine", "1/10/1970", "HB12345")
#
# # Le tournoi est créé.
# tournament = Tournament("T01", "Le Grand échiquier", "Libreville", "01/12/2025", "")
# # Des joueurs s'incrivent au tournoi.
# tournament.add_player(player_1)
# tournament.add_player(player_2)
# tournament.add_player(player_3)
# tournament.add_player(player_4)
# tournament.add_player(player_5)
# tournament.add_player(player_6)
# tournament.add_player(player_7)
# tournament.add_player(player_8)
#
# print("")
# # Le tournoi génère les premiers matchs du premier tour et crée le premier tour.
# round_ = Round(tournament.get_match())
# # Le tour est joué.
# round_.auto_play()
# print(round_.get_match_resume())
# tournament.add_round(round_)
# print(tournament.get_score())
#
# print("")
# # Le tournoi génère les matchs du tour suivant et crée le tour.
# round_ = Round(tournament.get_match())
# # Le tour est joué.
# round_.auto_play()
# print(round_.get_match_resume())
# tournament.add_round(round_)
# print(tournament.get_score())
#
# print("")
# # Le tournoi génère les matchs du tour suivant et crée le tour.
# round_ = Round(tournament.get_match())
# # Le tour est joué.
# round_.auto_play()
# print(round_.get_match_resume())
# tournament.add_round(round_)
# print(tournament.get_score())
#
# print("")
# # Le tournoi génère les matchs du tour suivant et crée le tour.
# round_ = Round(tournament.get_match())
# Le tour est joué.
# round_.auto_play()
# print(round_.get_match_resume())
# tournament.add_round(round_)
# print(tournament.get_score())

# liste de tout les tournois
tournament_list = []
player_list_all = []
player_list_tournament = []
tool = Tool()
tournament_active = None
controller = Controller(Display())
choice = controller.get_main_menu()

player_list_all.append(Player("Kasparov", "Garry", "13/04/1963", "AA00000"))
player_list_all.append(Player("Blue", "Deep", "15/05/1997", "XX00000"))
tournament_list.append(Tournament("T01", "Le Grand échiquier", "Libreville", "01/12/2025", ""))

while choice != "11":
    if choice == "1":
        # Créer un tournoi
        name = controller.get_input_tournament_name()
        # place = controller.get_input_tournament_place()
        tournament = Tournament("XX", name, "Libreville", "01/12/2025", "")
        tournament_list.append(tournament)
    elif choice == "2":
        # Démarrer un tournoi
        tournament_index = controller.get_list_tournament(tournament_list)
        index = int(tournament_index) - 1
        tournament = tournament_list[index]
        tool.set_main_tile(tournament.name)
        tournament_active = tournament
    elif choice == "3":
        # Saisir un nouveau joueur
        name = controller.get_input_player_name()
        player = Player(name, "XX", "XX", tool.get_national_id())
        player_list_all.append(player)
    elif choice == "4":
        # Ajouter un joueur au tournoi
        hint = controller.get_input_player_hint()
        player_list_hint = tool.get_list_player_from_hint(hint, player_list_all)
        player_index = controller.get_list_player(player_list_hint, player_list_all)
    elif choice == "5":
        # Débuter un tour
        # atttention, il faudra clôturer un tour pour calculer les scores
        confirmation = controller.get_confirmation()
        if confirmation in ("YES","yes"):
            match_liste = tournament_active.get_match()
            print(match_liste)
            os.system("pause")
            round_ = Round(match_liste)
            tournament_active.add_round(round_)
    elif choice == "6":
        # Saisir un résultat
        pass
    elif choice == "7":
        # Lister tous les joueurs
        pass
    elif choice == "8":
        # Lister tous les tournois
        pass
    elif choice == "9":
        # Lister tous les joueurs du tournoi
        pass
    elif choice == "10":
        # Lister les tours et les matches du tour
        controller.get_list_round_match(tournament_active)

    if tournament_active is None:
        choice = controller.get_main_menu()
    else:
        choice = controller.get_main_menu_tournament()
