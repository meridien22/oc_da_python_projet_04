import random
from .match import Match
from .player import Player


class Tournament:
    """
    Classe qui permet de gérer un tournoi d'échec.
    """
    # Nombre de tours par défaut du tournoi
    DEFAULT_NUMBER_ROUND = 4
    # Score d'un joueur qui gagne
    SCORE_WINNER = 1
    # Score d'un joueur qui perd
    SCORE_LOSER = 0
    # Score pour un match nul
    SCORE_DRAW = 0.5

    def __init__(self, id, name, place, date_start, description):
        self.id = id
        self.name = name
        self.place = place
        self.date_start = date_start
        self.player_list = []
        self.round_list = []
        self.description = description
        # liste qui stocke tous les identifiants des matchs
        # pour être sûr de ne pas rejouer un match
        self.id_matchs = []
        self.round_number = self.DEFAULT_NUMBER_ROUND
        # Permet de savoir si c'est le premier tour ou pas
        # car le tirage est différent
        self.first_round = False

    def __str__(self):
        return f"Tournoi {self.name} du {self.date_start} à {self.place}"

    def add_player(self, player):
        self.player_list.append(player)

    def add_round(self, round_):
        self.round_list.append(round_)

    def calculate_score(self, round_):
        for match in round_.match_list:
            if isinstance(match.winner, Player):
                if match.player_1 == match.winner:
                    match.player_1.score += self.SCORE_WINNER
                    match.player_2.score += self.SCORE_LOSER
                else:
                    match.player_2.score += self.SCORE_WINNER
                    match.player_1.score += self.SCORE_LOSER
            else:
                match.player_1.score += self.SCORE_DRAW
                match.player_2.score += self.SCORE_DRAW

    def get_score(self):
        """Retourne les joueurs du tournoi et leurs scores"""
        self.player_list.sort(key=lambda element: element.score, reverse=True)
        player_list = []
        for player in self.player_list:
            player_list.append(f"{str(player)} ({player.score})")
        return player_list

    def get_rounds_matchs(self):
        """Retourne les rounds du tournoi"""
        round_list = []
        for index, round_ in enumerate(self.round_list):
            round_list.append(f"Tour {index + 1} débuté à {str(round_)}")
            round_list.append(round_.get_match_resume())
        return round_list

    def get_match(self):
        """" Renvoi les matches d'un tour
        1er tour : tirage aléatoire
        tour suivant : tirage score => tirage logique => tirage aléatoire"""

        # si c'est le premier match, on mélange les joueurs aléatoirement
        if self.first_round:
            random.shuffle(self.player_list)
            self.first_round = False
        # sinon on trie les joueurs en fonction de leurs scores
        else:
            self.player_list.sort(key=lambda element: element.score)

        draw = self.get_draw()
        index_modifier = 1
        while draw == "Echec":
            draw = self.get_draw()
            # tirage logique en essayant de respecter le plus possible
            # le tri par score
            if index_modifier < len(self.player_list):
                # on soustrait à la liste le joueur qui correxpond
                # à l'index modifieur
                player_modifier = self.player_list.pop(index_modifier)
                # on l'insert dans la liste à la position suivante
                self.player_list.insert(index_modifier + 1, player_modifier)
                index_modifier += 1
            # tirage aléatoire car la méthode précédnte a échoué
            else:
                random.shuffle(self.player_list)

        return draw

    def get_draw(self):
        """Propose un tirage pour un tour"""
        index_player_1 = 0
        index_player_2 = 1
        match_list = []

        while index_player_2 < len(self.player_list):
            index_search = index_player_2
            player_1 = self.player_list[index_player_1]
            player_2 = self.player_list[index_player_2]
            match = Match(player_1, player_2)

            # cas où le match a déjà été joué
            while match.id in self.id_matchs:
                # cas ou l'algorithme n'a pas réussi à proposer
                # une combinaison cohérente car
                # l'index de recherce est arrivé au bout de la liste
                if index_search + 1 == len(self.player_list):
                    return "Echec"
                # on soustrait à la liste le joueur qui vient après le joueur 2
                player_next = self.player_list.pop(index_search + 1)
                # on l'insert dans la liste après le joueur 1
                self.player_list.insert(index_player_1 + 1, player_next)
                # on crée un nouveau match pour pouvoir tester
                # s'il a déjà été joué ou non
                player_1 = self.player_list[index_player_1]
                player_2 = self.player_list[index_player_2]
                match = Match(player_1, player_2)
                # on incrémente l'index de recherche de 1 pour aller chercher
                # le prochain candididat si le match a déjà été joué
                index_search += 1

            match_list.append(match)
            index_player_1 += 2
            index_player_2 += 2

        # on ajoute les identifiants des macthes à la liste id_matchs
        # permet d'avoir un suivi des matches déjà joués
        for match in match_list:
            self.id_matchs.append(match.id)
        return match_list
