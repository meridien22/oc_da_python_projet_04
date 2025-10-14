class Player:
    """Crée un joueur pouvant participer au tournoi"""

    def __init__(self, name, first_name, date_birth, id_national):
        self.name = name
        self.first_name = first_name
        self.date_birth = date_birth
        self.id_national = id_national

    def __str__(self):
        return f"{self.first_name} {self.name} ({self.id_national})"

    def __repr__(self):
        return str(self)

    @classmethod
    def from_dict(cls, data):
        """Renvoi un joueur sous forme de liste"""
        return Player(data["name"],
                      data["first_name"],
                      data["date_birth"],
                      data["id_national"])

    def to_dict(self):
        """Créer un objet Player à partir d'une liste"""
        return {
            "name": self.name,
            "first_name": self.first_name,
            "date_birth": self.date_birth,
            "id_national": self.id_national
        }
