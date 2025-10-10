import random
from .match import Match
from .player import Player
from .round import Round


class Tournament:
    """
    Classe qui permet de gérer un tournoi d'échec.
    """
    # Nombre de tours par défaut du tournoi
    DEFAULT_NUMBER_ROUND = 2
    # Score par défaut d'un joueur en début de tournoi
    SCORE_BASE = 0
    # Score d'un joueur qui gagne
    SCORE_WINNER = 1
    # Score d'un joueur qui perd
    SCORE_LOSER = 0
    # Score pour un match nul
    SCORE_DRAW = 0.5

    def __init__(self, id, name, location, date_start, description):
        self.id = id
        self.name = name
        self.location = location
        self.date_start = date_start
        self.player_list = []
        self.round_list = []
        self.description = description
        self.round_number = self.DEFAULT_NUMBER_ROUND


    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "location" : self.location,
            "date_start" : self.date_start,
            "description" : self.description,
            "player_list" : self.player_list,
            "round_list" : [round_.to_dict() for round_ in self.round_list]
        }

    def __str__(self):
        return f"Tournoi {self.name} du {self.date_start} à {self.location}"

    def add_player(self, player):
        self.player_list.append({
            "id_national" : player.id_national,
            "score" : self.SCORE_BASE,
            "opponent_list" : []
        })

    def calculate_score(self, match):
        if match.player_1 == match.winner:
            self.add_point(match.player_1, self.SCORE_WINNER)
            self.add_point(match.player_2, self.SCORE_LOSER)
        elif match.player_2 == match.winner:
            self.add_point(match.player_2, self.SCORE_WINNER)
            self.add_point(match.player_1, self.SCORE_LOSER)
        else:
            self.add_point(match.player_1, self.SCORE_DRAW)
            self.add_point(match.player_2, self.SCORE_DRAW)

    def add_point(self, player, point):
        for player_tournament in self.player_list:
            if player_tournament["id_national"] == player:
                player_tournament["score"] += point

