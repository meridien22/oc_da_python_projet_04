import random


class Match:

    def __init__(self, player_1, player_2):
        """Initialise un match entre 2 joueurs avec un score de 0"""
        self.player_1 = player_1
        self.player_2 = player_2
        # identifiant unique d'un match
        self.id = self.get_id_match()
        self.winner = None

    def __str__(self):
        player_1_first_name = self.player_1.first_name
        player_2_first_name = self.player_2.first_name
        return (f"{player_1_first_name} contre {player_2_first_name} : "
                f"Gagnant => {str(self.winner)}")

    def get_id_match(self):
        """Retourne l'identifiant unique d'un match en fonction des
        identifiants des joueurs classés par ordre alphabétique"""
        if self.player_1 < self.player_2:
            return self.player_1.id_national + "_" + self.player_2.id_national
        else:
            return self.player_2.id_national + "_" + self.player_1.id_national

    def get_player_opposite(self, player):
        """Retourne le joueur adverse"""
        if self.player_1 == player:
            return self.player_2
        else:
            return self.player_1

    def get_winner(self):
        """Retourne le gagnant aleatoire du match
        ou None en cas de match nul.
        Si le joueur est Garry Kasparov, il gagne à chaque fois.
        Si le joueur est Deep Blue, il perd à chaque fois."""
        player_name_1 = self.player_1.first_name + " " + self.player_1.name
        player_name_2 = self.player_2.first_name + " " + self.player_2.name
        if player_name_1 == "Garry Kasparov":
            return self.player_1
        elif player_name_2 == "Garry Kasparov":
            return self.player_2
        if player_name_1 == "Deep Blue":
            return self.player_2
        elif player_name_2 == "Deep Blue":
            return self.player_1
        else:
            tirage = random.randint(0, 2)
            if tirage == 1:
                return self.player_1
            elif tirage == 2:
                return self.player_2
            else:
                return None
