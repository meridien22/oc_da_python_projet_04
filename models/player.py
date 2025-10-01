class Player:
    """Crée un joueur pouvant participer au tournoi"""

    # Score par défaut d'un joueur en début de tournoi
    SCORE_BASE = 0

    def __init__(self, nom, first_name, date_birth, id_national):
        self.name = nom
        self.first_name = first_name
        self.date_birth = date_birth
        self.id_national = id_national
        self.score = self.SCORE_BASE

    def __str__(self):
        return f"{self.first_name} {self.name}"

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.id_national < other.id_national

    def __eq__(self, other):
        return self.id_national == other.id_national