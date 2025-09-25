class Tournoi:

    # Nombre de tours par défaut du tournoi
    NOMBRE_TOURS_DEFAUT = 4

    def __init__(self, identifiant, nom, lieu, date_debut, description):
        self.identifiant = identifiant
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.joueurs = []
        self.description = description
        self.nombre_tour = self.NOMBRE_TOURS_DEFAUT

    def __str__(self):
        return (f"Tournoi {self.nom} du {self.date_debut} "
                f"à {self.lieu}: {len(self.joueurs)} joueurs.")

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)