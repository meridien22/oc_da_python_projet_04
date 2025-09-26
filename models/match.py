import random

class Match:

    # Score d'un joueur en début de match
    SCORE_BASE = 0
    # Score d'un joueur qui gagne
    SCORE_GAGNANT = 1
    # Score d'un joueur qui perd
    SCORE_PERDANT = 0
    # Score pour un match nul
    SCORE_MATCH_NUL = 0.5

    def __init__(self, tournoi, tour, joueur_score_1, joueur_score_2):
        """Initialise un match entre 2 joueurs avec un score de 0"""
        self.participants = (joueur_score_1, joueur_score_2)
        # identifiant unique d'un match
        self.identifiant = self.get_idendifiant(joueur_score_1[0], joueur_score_2[0])

    def __str__(self):
        joueur_1 = self.get_joueur_1()
        joueur_2 = self.get_joueur_2()
        return f"{joueur_1.prenom} contre {joueur_2.prenom}"

    def get_idendifiant(self, joueur1, joueur2):
        """Retourne l'identifiant unique d'un match en fonction des
        identifiants des joueurs classés par ordre alphabétique"""
        if joueur1 < joueur2:
            return joueur1.identifiant_national + "_" + joueur2.identifiant_national
        else:
            return joueur2.identifiant_national + "_" + joueur1.identifiant_national

    def get_joueur_1(self):
        """Retourne le premier joueur du match"""
        return self.participants[0][0]

    def get_joueur_2(self):
        """Retourne le deuxième joueur du match"""
        return self.participants[1][0]

    def get_autre_joueur(self, joueur):
        """Retourne le joueur adverse"""
        if self.get_joueur_1() == joueur:
            return self.get_joueur_2()
        else:
            return self.get_joueur_1()

    def get_score_joueur_1(self):
        """Retourne le scrore du premier joueur du match"""
        return self.participants[0][1]

    def get_score_joueur_2(self):
        """Retourne le score du deuxième joueur du match"""
        return self.participants[1][1]

    def ajouter_score(self, joueur, score):
        """Ajoute un score à un joueur du match"""
        if self.get_joueur_1() == joueur:
            self.participants[0][1] += score
        else:
            self.participants[1][1] += score

    def get_gagnant_aleatoire(self):
        """Retourne le gagnant aleatoire du match
        ou None en cas de match nul.
        Si le joueur est Garry Kasparov, il gagne à chaque fois.
        Si le joueur est Deep Blue, il perd à chaque fois."""
        joueur_1 = self.get_joueur_1()
        joueur_2 = self.get_joueur_2()
        nom_joueur_1 = joueur_1.prenom + " " + joueur_1.nom
        nom_joueur_2 = joueur_2.prenom + " " + joueur_2.nom
        if nom_joueur_1 == "Garry Kasparov":
            return joueur_1
        elif nom_joueur_2 == "Garry Kasparov":
            return joueur_2
        if nom_joueur_1 == "Deep Blue":
            return joueur_2
        elif nom_joueur_2 == "Deep Blue":
            return joueur_1
        else:
            tirage = random.randint(0, 2)
            if  tirage == 1:
                return joueur_1
            elif tirage == 2:
                return joueur_2
            else:
                return None