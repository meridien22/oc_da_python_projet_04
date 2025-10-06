
class Player:
    """Crée un joueur pouvant participer au tournoi"""

    def __init__(self, name, first_name, date_birth, id_national):
        self.name = name
        self.first_name = first_name
        self.date_birth = date_birth
        self.id_national = id_national

    def __str__(self):
        return f"{self.first_name} {self.name}"

    def __repr__(self):
        return str(self)

