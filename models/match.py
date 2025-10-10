import random


class Match:

    def __init__(self, player_1, player_2):
        """Initialise un match entre 2 joueurs avec un score de 0"""
        self.player_1 = player_1
        self.player_2 = player_2
        self.winner = None

    def __str__(self):
        return (f"{self.player_1 } "
                f"contre "
                f"{self.player_2} : "
                f"Gagnant => {self.winner}")

    def to_dict(self):
        return {
            "player_1": self.player_1,
            "player_2": self.player_2,
            "winner": self.winner
        }

    def get_winner(self):
        """Retourne le gagnant aleatoire du match
        ou None en cas de match nul.
        Si le joueur est Garry Kasparov, il gagne à chaque fois.
        Si le joueur est Deep Blue, il perd à chaque fois."""
        if self.player_1 == "AA00000":
            return self.player_1
        elif self.player_2 == "AA00000":
            return self.player_2
        if self.player_1 == "XX00000":
            return self.player_2
        elif self.player_2 == "XX00000":
            return self.player_1
        else:
            tirage = random.randint(0, 2)
            if tirage == 1:
                return self.player_1
            elif tirage == 2:
                return self.player_2
            else:
                return 0
