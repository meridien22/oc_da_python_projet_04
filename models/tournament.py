import uuid
import datetime
from .round import Round


class Tournament:
    """Classe qui permet de gérer un tournoi d'échec"""

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

    def __init__(self, name, location, date_start,
                 description, round_number=DEFAULT_NUMBER_ROUND,
                 id=None, player_list=None, round_list=None):
        if id is None:
            # on convertit l'uuid en chaîne car ce n'est pas possible de serialiser un tel objet
            self.id = str(uuid.uuid4())
        else:
            self.id = id
        self.name = name
        self.location = location
        if date_start is None:
            self.date_start = datetime.datetime.now().strftime("%d/%m/%Y")
        else:
            self.date_start = date_start
        self.description = description
        self.round_number = round_number
        if player_list is None:
            self.player_list = []
        else:
            self.player_list = player_list
        if round_list is None:
            self.round_list = []
        else:
            self.round_list = round_list

    def to_dict(self):
        """Renvoi un Tournoi sous forme de liste"""
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "date_start": self.date_start,
            "description": self.description,
            "round_number": self.round_number,
            "player_list": self.player_list,
            "round_list": [round_.to_dict() for round_ in self.round_list]
        }

    @classmethod
    def from_dict(cls, data):
        """Créer un objet Tournoi à partir d'une liste"""
        return cls(
            data["name"],
            data["location"],
            data["date_start"],
            data["description"],
            data["round_number"],
            data["id"],
            data["player_list"],
            [Round.from_dict(round_data) for round_data in data["round_list"]]
        )

    def __str__(self):
        return f"Tournoi {self.name} du {self.date_start} à {self.location}"

    def add_player(self, player):
        """Ajoute un joueur au tournoi"""
        self.player_list.append({
            "id_national": player.id_national,
            "score": self.SCORE_BASE,
            "opponent_list": []
        })

    def calculate_score(self, match):
        """Calcul le score des joueurs à l'issue d'un match"""
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
        """Ajoute des points à un joueur"""
        for player_tournament in self.player_list:
            if player_tournament["id_national"] == player:
                player_tournament["score"] += point
