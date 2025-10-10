from controllers import *
from models import *


# liste de tous les tournois
tournament_list = []
# liste de tous les joueurs
player_list_all = [Player("Kasparov", "Garry", "13/04/1963", "AA00000"),
                   Player("Blue", "Deep", "15/05/1997", "XX00000"),
                   Player("Lucas", "George", "01/05/1997", "BB00000"),
                   Player("Connor", "Sarah", "01/02/1995", "FF00000"),
                   Player("Jackson", "Peter", "01/06/1998", "CC00000"),
                   Player("Tyson", "Mike", "01/07/1999", "DD00000"),
                   Player("Balboa", "Rocky", "01/02/1995", "EE00000"),
                   Player("Le Guin", "Ursula", "12/12/1212", "GG00000")]

manager_tool = ManagerTool()
manager_choice = ManagerChoice(manager_tool)
manager_text = ManagerText(manager_tool)
manager_content = ManagerContent(manager_tool)

def start_tournament():
    # tournoi actif
    tournament = Tournament("T01", "Le Grand échiquier", "Libreville","01/12/2025", "")
    tournament_list.append(tournament)
    # joueurs inscrits
    tournament.add_player(player_list_all[0])
    tournament.add_player(player_list_all[1])
    tournament.add_player(player_list_all[2])
    tournament.add_player(player_list_all[3])

    choice = None
    while choice != "12":
        choice = manager_choice.get_main_menu(tournament)
        match choice:
            # Créer un tournoi
            case "1":
                tournament = manager_text.get_tournament()
                tournament_list.append(tournament)
            # Saisir un nouveau joueur
            case "2":
                player = manager_text.get_new_player()
                player_list_all.append(player)
            # Activer un tournoi
            case "3":
                if not manager_tool.tournament_to_activate(tournament_list):
                    manager_tool.get_information(1)
                else:
                    tournament = manager_choice.get_tournament_choice(tournament_list)
            # Inscrire un joueur
            case "4":
                check_inscriptin_open = manager_tool.check_inscriptin_open(tournament, player_list_all)
                if check_inscriptin_open != 0:
                    manager_tool.get_information(check_inscriptin_open)
                else :
                    if manager_tool.inscriptipn_can_continue(tournament, player_list_all):
                        player = manager_choice.get_inscription(tournament, player_list_all)
                        if player is not None:
                            tournament.add_player(player)
                    else:
                        manager_tool.get_information("11")
            # Démarrer un tour
            case "5":
                # Le tournoi n'est pas commencé
                if tournament is None:
                    manager_tool.get_information("2")
                # Il y a un tour en cours
                elif manager_tool.round_in_progress(tournament):
                    manager_tool.get_information("5")
                # Le nombre de tours maximum a été atteint
                elif manager_tool.is_max_round(tournament):
                    manager_tool.get_information("6", tournament.round_number)
                # Le nombre inscrit est impair
                elif not manager_tool.player_register_even_number(tournament):
                    manager_tool.get_information("15")
                else:
                    if manager_tool.list_player_compatible_with_number_round(tournament.player_list):
                        if len(tournament.round_list) == 0:
                            message = InformationUser.get_message("8")
                            confirmation = manager_text.get_confirmation(message)
                            if confirmation:
                                manager_tool.add_round(tournament)
                                manager_content.get_round_resume(tournament, player_list_all)
                        else:
                            manager_tool.add_round(tournament)
                            manager_content.get_round_resume(tournament, player_list_all)
                    else:
                        manager_tool.get_information("9")
            # Saisir des résultats
            case "6":
                if manager_tool.last_round_finish(tournament):
                    manager_tool.get_information("14")
                elif not manager_tool.round_in_progress(tournament):
                    manager_tool.get_information("13")
                else:
                    manager_choice.get_enter_result(tournament, player_list_all)
            # Résumé des tours
            case "7":
                # Le tournoi n'est pas commencé
                if tournament is None:
                    manager_tool.get_information("2")
                # Il n'y a aucun tour
                elif len(tournament.round_list) == 0:
                    manager_tool.get_information("12")
                else:
                    manager_content.get_round_resume(tournament, player_list_all)
            # Liste des joueus inscrits
            case "8":
                if tournament is None:
                    manager_tool.get_information("2")
                elif len(tournament.player_list) == 0:
                    manager_tool.get_information("10")
                else:
                    manager_content.get_player_register(player_list_all, tournament)
            # Liste tous les joueurs
            case "9":
                manager_content.get_player_full(player_list_all)
            # Lister tous les tournois
            case "10":
                manager_content.get_tournament_full(tournament_list)
            # Classement du tournoi
            case "11":
                if tournament is None:
                    manager_tool.get_information("2")
                elif len(tournament.player_list) == 0:
                    manager_tool.get_information("10")
                else:
                    manager_content.get_ranking(tournament, player_list_all)
            # Quitter
            case "12":
                break

start_tournament()