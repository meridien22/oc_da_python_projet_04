import datetime


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
