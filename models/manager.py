from .tournament import Tournament

class TournamentManager:

    def __init__(self, tournament_list = None):
        if tournament_list is None:
            self.tournament_list = []
        else:
            self.tournament_list = tournament_list

    def to_dict(self):
        return {
            "tournament_list" : [tournament.to_dict() for tournament in self.tournament_list]
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            [Tournament.from_dict(tournament_data) for tournament_data in data["tournament_list"]]
        )