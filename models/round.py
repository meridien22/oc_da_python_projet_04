import datetime


class Round:
    """Créer un tour pour un tournoi d'échec"""
    def __init__(self, round_list,  match_list):
        self.date_time_start = self.get_date_time()
        self.date_time_end = None
        self.match_list = match_list
        self.name = self.get_name(round_list)

    def get_name(self, round_list):
        round_number = len(round_list) + 1
        return f"Tour {round_number}"

    def get_date_time(self):
        """Retourne la date du jour avec les heures et les minutes"""
        return datetime.datetime.now().strftime("%d/%m/%Y à %Hh%M")

    def finish(self):
        self.date_time_end = self.get_date_time()

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

    def is_finished(self):
        finished = True
        for match in self.match_list:
            if match.winner is None:
                finished = False
        return finished
