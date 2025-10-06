import random
from .match import Match
from .player import Player
from .round import Round


class Tournament:
    """
    Classe qui permet de gérer un tournoi d'échec.
    """
    # Nombre de tours par défaut du tournoi
    DEFAULT_NUMBER_ROUND = 4
    # Score par défaut d'un joueur en début de tournoi
    SCORE_BASE = 0
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
        self.id_national_list = []
        self.round_list = []
        self.description = description
        # liste qui stocke tous les identifiants des matchs
        # pour être sûr de ne pas rejouer un match
        self.id_matchs = []
        self.round_number = self.DEFAULT_NUMBER_ROUND

    def __str__(self):
        return f"Tournoi {self.name} du {self.date_start} à {self.place}"

    def add_player(self, player):
        self.player_list.append({
            "id_national" : player.id_national,
            "score" : self.SCORE_BASE,
            "opponent_list" : []
        })
        self.id_national_list.append(player.id_national)

    def add_round(self):
        # si il exsite un tour on le finit
        if len(self.round_list) > 0:
            roud_last = self.round_list[-1]
            roud_last.finish()

        match_list = self.get_match()
        round_ = Round(self.round_list, match_list)
        self.round_list.append(round_)

    def calculate_score(self, round_):
        for match in round_.match_list:
            if isinstance(match.winner, Player):
                if match.player_1 == match.winner:
                    self.add_point(match.player_1, self.SCORE_WINNER)
                    self.add_point(match.player_2, self.SCORE_LOSER)
                else:
                    self.add_point(match.player_2, self.SCORE_WINNER)
                    self.add_point(match.player_1, self.SCORE_LOSER)
            else:
                self.add_point(match.player_1, self.SCORE_DRAW)
                self.add_point(match.player_2, self.SCORE_DRAW)

    def add_point(self, player, point):
        for player_tournament in self.player_list:
            if player_tournament["id_national"] == player.id_national:
                player_tournament["score"] += point


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

        # si c'est le premier tour, on mélange les joueurs aléatoirement
        if len(self.round_list) == 0:
            random.shuffle(self.player_list)
        # sinon on trie les joueurs en fonction de leurs scores
        else:
            self.player_list.sort(key=lambda element: element["score"])

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
            # cas où le match a déjà été joué
            while player_2["id_national"] in player_1["opponent_list"]:

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
                # on incrémente l'index de recherche de 1 pour aller chercher
                # le prochain candididat si le match a déjà été joué
                index_search += 1
            match = Match(player_1["id_national"], player_2["id_national"])
            match_list.append(match)
            index_player_1 += 2
            index_player_2 += 2
        # sortie du while sans avoir rencontré d'échec,
        # on met à jour la liste des adversaires des joueurs
        self.update_opponent_list(match_list)
        return match_list

    def update_opponent_list(self, match_list):
        for match in match_list:
            for player_tournament in self.player_list:
                if player_tournament["id_national"] == match.player_1:
                    player_tournament["opponent_list"].append(match.player_2)
                else:
                    player_tournament["opponent_list"].append(match.player_1)