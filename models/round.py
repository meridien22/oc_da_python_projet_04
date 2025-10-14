import datetime
from .match import Match


class Round:
    """Créer un tour pour un tournoi d'échec"""

    def __init__(self,
                 name,
                 match_list=None,
                 date_time_start=None,
                 date_time_end=None):

        self.name = name
        if date_time_start is None:
            self.date_time_start = self.get_date_time()
        else:
            self.date_time_start = date_time_start
        self.date_time_end = date_time_end
        if isinstance(match_list, list):
            self.match_list = match_list
        else:
            self.match_list = []

    def to_dict(self):
        """Retourne un tour sous la forme d'une chaine de caratère json"""
        return {
            "name": self.name,
            "match_list": [match.to_dict() for match in self.match_list],
            "date_time_start": self.date_time_start,
            "date_time_end": self.date_time_end
        }

    @classmethod
    def from_dict(cls, data):
        """Construit un round à partir d'une chaine de caractère json"""
        return Round(data["name"],
                     [Match.from_dict(match_data) for match_data in data["match_list"]],
                     data["date_time_start"],
                     data["date_time_end"]
                     )

    def finish(self):
        """Met à jour la date/heure de fin d'un tour"""
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
        """Renvoi True si le march est fini"""
        finished = True
        for match in self.match_list:
            if match.winner is None:
                finished = False
        return finished

    def get_date_time(self):
        """Retourne la date du jour avec les heures et les minutes"""
        return datetime.datetime.now().strftime("%d/%m/%Y à %Hh%M")
