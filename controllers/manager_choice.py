from views import (MenuMain,
                   MenuTournamentChoice,
                   MenuInscriptionPlayer,
                   MenuEnterResult,
                   MenuEnterMacthResult,
                   MenuHint)
from controllers import ManagerTool


class ManagerChoice:

    FIND_ALL = "*"

    def __init__(self, display):
        self.manager_tool = ManagerTool()

    def get_main_menu(self, tournament=None):
        """Renvoi le choix de l'utilisateur dans le menu principal"""
        menu = MenuMain()
        return menu.execute(tournament)

    def get_tournament_choice(self, tournament_list):
        """Renvoi le tournoi sélectionné parmi une liste de tournoi"""
        tournamet_display = []
        for tournament in tournament_list:
            tournamet_display.append(tournament)
        menu = MenuTournamentChoice()
        choice = menu.execute(tournamet_display)
        return tournamet_display[int(choice) - 1]

    def get_inscription(self, tournament, player_list):
        """Renvoi un joueur sélectionné parmi une liste de joueur"""
        # On demande à l'utilisateur ses critères de recherche
        menu = MenuHint()
        hint = menu.execute(tournament.name)

        player_filter_list = []
        # on contrôle d'abord que le joueur ne soit pas déjà inscrit
        for player in player_list:
            if player.id_national not in self.manager_tool.get_list_id_national(tournament):
                player_filter_list.append(player)

        # on fait une recherche dans le nom et dans le prénom si demandé
        player_filter_hint_list = []
        if hint != self.FIND_ALL:
            player_filter_hint_list = self.manager_tool.get_player_from_hint(hint, player_filter_list)
        else:
            player_filter_hint_list = player_filter_list

        # si la recherche ne renvoie aucun résultat, on renvoie la premmière liste filtrée
        if len(player_filter_hint_list) == 0:
            player_filter_hint_list = player_filter_list

        # on gère maintenant l'affichage des résultats par page

        # Nombre d'éléments que le veut afficher par page
        number_player_display = 15
        # Index de départ de la liste pour la page en cours
        index_start = 0
        # Index de fin de la liste pour la page en cours
        index_end = 0
        # La première page est la page 1
        page = 1
        # On fait une division entière de la longeur de la liste par le nombre d'éléments que l'on veut
        # afficher par page. Le quotient représente le nombre de fois que l'on peut afficher une
        # page complète et le reste représente la dernière page
        part, rest = divmod(len(player_filter_hint_list), number_player_display)
        if rest > 0:
            rest = 1
        else:
            rest = 0
        page_full = part + rest

        # tant que l'index de fin ne dépasse pas la longueur de la liste
        while index_end < len(player_filter_hint_list):
            # On extrait de la liste la partie qui nous intéresse
            # On faisant cela, on perd les index d'origine
            index_end = index_start + number_player_display
            list_extract = player_filter_hint_list[index_start:index_end]
            # Pour retrouver les index d'origin, on repart de la liste de départ
            # Et on ne retient que ceux qui sont dans la liste extraite
            display_dict = {}
            for index, player in enumerate(player_filter_hint_list):
                if player in list_extract:
                    display_dict[index] = player
            menu = MenuInscriptionPlayer()
            choice = menu.execute(tournament.name, display_dict, page, page_full)
            # Si le choix est un entier, on sort de la boucle et on retient ce choix
            try:
                int(choice)
                return player_filter_hint_list[int(choice) - 1]
            except ValueError:
                pass
            # Si le choix est "s" on va à la page suivante
            if choice == "s":
                index_start += number_player_display
                page += 1
            # Si le choix est "r" ou si on est à la dernière page, on repart au début
            if choice == "r" or page == page_full + 1:
                index_start = 0
                index_end = 0
                page = 1
            # Si le choix est "a" on interrompt la procédure d'inscription
            if choice == "a" or page == page_full + 1:
                return None

    def get_enter_result(self, tournament, player_list):
        """Permet de choisir un match dans une liste puis de désigner un vainqueur"""
        round_ = tournament.round_list[-1]
        action_dict = {}
        match_for_result_list = []
        for index, match in enumerate(round_.match_list):
            if match.winner is None:
                match_for_result_list.append(match)

        for index, match in enumerate(match_for_result_list):
            player_1 = self.manager_tool.get_player_from_id(player_list, match.player_1)
            player_2 = self.manager_tool.get_player_from_id(player_list, match.player_2)
            action_dict[str(index + 1)] = str(player_1) + " contre " + str(player_2)

        menu = MenuEnterResult()
        match_index = menu.execute(action_dict, tournament.name, round_.name)
        match_index = int(match_index) - 1
        match = match_for_result_list[match_index]

        action_dict = {}
        player_1 = self.manager_tool.get_player_from_id(player_list, match.player_1)
        player_2 = self.manager_tool.get_player_from_id(player_list, match.player_2)
        action_dict["1"] = player_1
        action_dict["2"] = player_2
        action_dict["3"] = "Match nul"

        menu = MenuEnterMacthResult()
        choice = menu.execute(action_dict, tournament.name, round_.name)

        match choice:
            case "1":
                match.winner = player_1.id_national
            case "2":
                match.winner = player_2.id_national
            case "3":
                match.winner = 0

        tournament.calculate_score(match)

        # si le tour est terminé, on met à jour la date de fin
        if not self.manager_tool.round_in_progress(tournament):
            round_.finish()
            self.manager_tool.get_information("16")
