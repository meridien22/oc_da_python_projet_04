class Tournoi:
    """
    Classe qui permet de gérer un tournoi d'échec.
    """
    # Nombre de tours par défaut du tournoi
    NOMBRE_TOURS_DEFAUT = 4
    # Score par défaut d'un joueur en début de tournoi
    SCORE_DEFAUT = 0

    def __init__(self, identifiant, nom, lieu, date_debut, description):
        self.identifiant = identifiant
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.joueurs_scores = []
        self.description = description
        # liste qui stocke tous les identifiants des matchs pour être sûr de ne pas rejouer un match
        self.identifiant_matchs = []
        self.nombre_tour = self.NOMBRE_TOURS_DEFAUT

    def __str__(self):
        return (f"Tournoi {self.nom} du {self.date_debut} "
                f"à {self.lieu}: {len(self.joueurs_scores)} joueurs.")

    def ajouter_joueur_score(self, joueur, score = SCORE_DEFAUT):
        self.joueurs_scores.append([joueur, score])

    def get_score(self):
        """Donne les scores des joueurs pour le tour"""
        return self.joueurs_scores