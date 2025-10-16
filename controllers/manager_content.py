from controllers import ManagerTool
from views import MenuPlayerList, MenuRoundResume


class ManagerContent:
    def __init__(self, display):
        self.manager_tool = ManagerTool()

    def get_player_register(self, player_list, tournament):
        """Affiche la liste des joueurs inscrits"""
        player_display_list = []
        player_num = 1
        for player_id_national in self.manager_tool.get_list_id_national(tournament):
            player = self.manager_tool.get_player_from_id(player_list, player_id_national)
            row = [player_num, player.first_name, player.name, player.date_birth, player.id_national]
            player_display_list.append(row)
            player_num += 1
        player_list_tri = sorted(player_display_list, key=lambda element: element[0])
        menu = MenuPlayerList()
        return menu.execute(tournament.name, player_list_tri)

    def get_player_full(self, player_list):
        """Affiche la liste des tous les joueurs de la fédération"""
        player_display_list = []
        header_list = ["Prénom", "Nom", "Date de naissance", "Id national"]
        title = "Liste de tous les joueurs de la fédération"
        for player in player_list:
            row = [player.first_name, player.name, player.date_birth, player.id_national]
            player_display_list.append(row)
        player_list_tri = sorted(player_display_list, key=lambda element: element[1])
        self.manager_tool.get_list_paginated(title, header_list, player_list_tri, 15)

    def get_tournament_full(self, tournament_list):
        """Affiche la liste de tous les tournois"""
        tournament_display_list = []
        header_list = ["Nom", "Emplacement", "Date", "Round", "Joueurs"]
        title = "Liste de tous les tournois de la fédération"
        for tournament in tournament_list:
            row = [
                tournament.name,
                tournament.location,
                tournament.date_start,
                tournament.round_number,
                len(tournament.player_list)
            ]
            tournament_display_list.append(row)

        self.manager_tool.get_list_paginated(title, header_list, tournament_display_list, 10)

    def get_round_resume(self, tournament, player_list, pause=True):
        """Affiche le résumé des tours"""
        round_display_list = []
        for round_ in tournament.round_list:
            row = [round_.name, round_.date_time_start, round_.date_time_end, len(round_.match_list)]
            round_display_list.append(row)

        match_display = []
        roud_last = tournament.round_list[-1]
        for match in roud_last.match_list:
            player_1 = self.manager_tool.get_player_from_id(player_list, match.player_1)
            player_2 = self.manager_tool.get_player_from_id(player_list, match.player_2)
            if match.winner == 0:
                winner = "Match nul"
            else:
                winner = self.manager_tool.get_player_from_id(player_list, match.winner)
            row = [player_1, player_2, winner]
            match_display.append(row)

        menu = MenuRoundResume()
        return menu.execute(tournament.name, roud_last.name, round_display_list, match_display, pause)

    def get_round_ranking(self, tournament, player_list):
        """Affiche les détails du dernier round et le classement général"""
        pause = False
        self.get_round_resume(tournament, player_list, pause)
        clear = False
        self.get_ranking(tournament, player_list, clear)

    def get_ranking(self, tournament, player_list, clear=True):
        """Donne le classement d'un tournoi"""
        player_tri = sorted(tournament.player_list, key=lambda element: element["score"], reverse=True)
        player_display_list = []
        header_list = ["Joueurs", "Score"]
        title = "Classement général"
        for player in player_tri:
            id_national = player["id_national"]
            score = player["score"]
            player = self.manager_tool.get_player_from_id(player_list, id_national)
            row = [player, score]
            player_display_list.append(row)

        self.manager_tool.get_list_paginated(title, header_list, player_display_list, 10, clear)
