import random


class Match:
    """Crée un match entre 2 joueurs"""

    def __init__(self, player_1_id_national, player_2_id_national, winner=None):
        self.player_1 = player_1_id_national
        self.player_2 = player_2_id_national
        self.winner = winner

    def __str__(self):
        return (f"{self.player_1} "
                f"contre "
                f"{self.player_2} : "
                f"Gagnant => {self.winner}")

    @classmethod
    def from_dict(cls, data):
        """Renvoi un match sous forme de liste"""
        return Match(data["player_1_id_national"],
                     data["player_2_id_national"],
                     data["winner"])

    def to_dict(self):
        """Créer un objet Match à partir d'une liste"""
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

    def get_representation(self):
        """Retourne un tuple contenant deux listes, chacune contenant
        deux éléments : un joueur et un score"""
        if self.winner == self.player_1:
            tuple_ = ([self.player_1, 1], [self.player_1, 0])
        elif self.winner == self.player_2:
            tuple_ = ([self.player_1, 0], [self.player_1, 1])
        else:
            tuple_ = ([self.player_1, 0.5], [self.player_1, 0.5])
        return tuple_
