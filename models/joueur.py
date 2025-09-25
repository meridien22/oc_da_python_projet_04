class Joueur:
    """Crée un joueur pouvant participer au tournoi"""
    def __init__(self, nom, prenom, date_naissance, identifiant_national):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.identifiant_national = identifiant_national

    def __str__(self):
        return f"{self.prenom}"

    def __lt__(self, other):
        return self.identifiant_national < other.identifiant_national

    def __eq__(self, other):
        return self.identifiant_national == other.identifiant_national