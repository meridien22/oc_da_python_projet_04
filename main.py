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

# 2ème version

# liste de tout les tournois
# tournament_list = []
# player_list_all = []
# player_list_tournament = []
# tool = Tool()
# tournament_active = None
# round_active = None
# controller = Controller(Display())
# choice = controller.get_menu_choice("00")
#
# player_list_all.append(Player("Kasparov", "Garry", "13/04/1963", "AA00000"))
# player_list_all.append(Player("Blue", "Deep", "15/05/1997", "XX00000"))
# tournament_list.append(Tournament("T01", "Le Grand échiquier", "Libreville", "01/12/2025", ""))
#
# while choice != "12":
#     match choice:
#         case "1":
#             # Créer un tournoi
#             name = controller.get_menu_input("10")
#             # place = controller.get_menu_input("11")
#             tournament = Tournament("XX", name, "Libreville", "01/12/2025", "")
#             tournament_list.append(tournament)
#         case "2":
#             # Démarrer un tournoi
#             tournament_index = controller.get_list_tournament(tournament_list)
#             index = int(tournament_index) - 1
#             tournament = tournament_list[index]
#             tool.set_tile("001", tournament.name)
#             tournament_active = tournament
#         case "3":
#             # Saisir un nouveau joueur
#             name = controller.get_menu_input("30")
#             player = Player(name, "XX", "XX", tool.get_national_id())
#             player_list_all.append(player)
#         case "4":
#             # Ajouter un joueur au tournoi
#             hint = controller.get_menu_input("40")
#             player_list_hint = tool.get_list_player_from_hint(hint, player_list_all)
#             player_index = controller.get_list_player(player_list_hint, player_list_all)
#             player_index = int(player_index) - 1
#             tournament_active.add_player(player_list_all[player_index])
#         case "5":
#             # Débuter un tour
#             confirmation = controller.get_confirmation()
#             if confirmation:
#                 if len(tournament_active.round_list) > 0:
#                     round_last = tournament_active.round_list[-1]
#                     print(round_last.match_list)
#                     if round_last.is_finished():
#                         print("nouveau round1")
#                         tournament_active.add_round()
#                         round_active = tournament_active.round_list[-1]
#                     else:
#                         print("recupère round")
#                         round_active = round_last
#                 else:
#                     print("nouveau round2")
#                     tournament_active.add_round()
#                     round_active = tournament_active.round_list[-1]
#                 tool.set_tile("002", tournament_active.name + " " + round_active.name)
#                 os.system("pause")
#         case "6":
#             # Saisir un résultat
#             pass
#         case "7":
#             # Lister tous les joueurs
#             pass
#         case "8":
#             # Lister tous les tournois
#             pass
#         case "9":
#             # Lister tous les joueurs du tournoi
#             pass
#         case "10":
#             # Lister les tours et les matches du tour
#             controller.get_list_round_match(tournament_active)
#         case "11":
#             # Retour au menu principal
#             round_active = None
#             tournament_active = None
#
#     match tool.get_tournament_statement(tournament_active, round_active):
#         case tool.TOURNAMENT_NOT_STARTING:
#             choice = controller.get_menu_choice("00")
#         case tool.TOURNAMENT_STARTING:
#             choice = controller.get_menu_choice("001")
#         case tool.ROUND_STARTING:
#             choice = controller.get_menu_choice("002")

# 3ème version

# liste de tous les tournois
tournament_list = []
# liste de tous les joueurs
player_list_all = []
# boite à outils, en faire un controlleur de tournoi ?
tool = Tool()

player_list_all.append(Player("Kasparov", "Garry", "13/04/1963", "AA00000"))
player_list_all.append(Player("Blue", "Deep", "15/05/1997", "XX00000"))
player_list_all.append(Player("Poilpré", "Olivier", "01/05/1997", "BB00000"))
player_list_all.append(Player("Popol", "Lucas", "01/05/1997", "CC00000"))

controller = Controller(Display())

def start_test():
    tournament = Tournament("T01", "Le Grand échiquier", "Libreville","01/12/2025", "")
    tournament_list.append(tournament)
    tournament.add_player(player_list_all[0])
    tournament.add_player(player_list_all[1])
    tournament.add_player(player_list_all[2])
    tournament.add_player(player_list_all[3])
    tournament.add_round()

    round_ = tournament.round_list[-1]
    for match in round_.match_list:
        match.winner = match.player_1

    tournament.add_round()

    round_ = tournament.round_list[-1]
    for match in round_.match_list:
        match.winner = match.player_1

    controller.get_round_resume(tournament, player_list_all)


def start_tournament():
    choice = None
    while choice != "99":
        choice = controller.get_main_menu()
        if choice == "1":
            if tool.tournament_to_restart(tournament_list):
                # on reprend le dernier tournoi de la liste
                tournament = tournament_list[-1]
            else:
                tournament = Tournament("T01", "Le Grand échiquier", "Libreville","01/12/2025", "")
                tournament_list.append(tournament)

            if not tool.inscription_finished(tournament):
                choice = controller.get_menu_inscription(tournament, player_list_all)
                while choice != "2":
                    match choice:
                        case "1":
                            player = controller.get_inscription(tournament, player_list_all)
                            tournament.add_player(player)
                            choice = controller.get_menu_inscription(tournament, player_list_all)
                        case "2":
                            pass
                        case "3":
                            controller.get_player_register(player_list_all, tournament)
                            choice = controller.get_menu_inscription(tournament, player_list_all)
                        case "4":
                            controller.get_player_other(player_list_all, tournament)
                            choice = controller.get_menu_inscription(tournament, player_list_all)
                        case "0":
                            break

            if not tool.round_in_progress(tournament) and choice != '0':
                tournament.add_round()

            while tool.round_in_progress(tournament) and choice != '0':
                choice = controller.get_menu_round(tournament, player_list_all)
                match choice:
                    case "1":
                        controller.get_enter_result(tournament, player_list_all)
                    case "2":
                        break


# start_tournament()
start_test()