import random


class Match:

    def __init__(self, player_1_id_national, player_2_id_national, winner = None):
        """Initialise un match entre 2 joueurs avec un score de 0"""
        self.player_1 = player_1_id_national
        self.player_2 = player_2_id_national
        self.winner = None

    def __str__(self):
        return (f"{self.player_1 } "
                f"contre "
                f"{self.player_2} : "
                f"Gagnant => {self.winner}")

    @classmethod
    def from_dict(cls, data):
        return Match(data["player_1_id_national"],
                     data["player_2_id_national"],
                     data["winner"])

    def to_dict(self):
        return {
            "player_1_id_national": self.player_1,
            "player_2_id_national": self.player_2,
            "winner": self.winner
        }

    def get_winner(self):
        """Retourne le gagnant aleatoire du match
        ou None en cas de match nul."""
        tirage = random.randint(0, 2)
        if tirage == 1:
            return self.player_1
        elif tirage == 2:
            return self.player_2
        else:
            return 0
