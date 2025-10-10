class TournamentManager:

    def __init__(self):
        self.tournament_list = []

    def to_dict(self):
        return {
            "tournament_list" : [tournament.to_dict() for tournament in self.tournament_list]
        }