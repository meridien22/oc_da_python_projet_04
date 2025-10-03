display_parameters ={
    # Menu général de base de l'application
    "00" : {
        "title" : "-------------------CHESS MASTER PRO ULTIMATE-------------------",
        "content" : None,
        "actions" : {
            "1" : "Créer un tournoi",
            "2" : "Démarrer un tournoi",
            "3" : "Saisir un nouveau joueur",
            "7" : "Lister tous les joueurs",
            "8" : "Lister tous les tournois",
            "12" : "Quitter"
        },
        "input": "None",
        "input_choice" : "Entrez le numéro de votre choix : "
    },
    # Menu lorsqu'un tournoi est démarré mais pas un tour
    "001": {
        "title": None,
        "content": None,
        "actions": {
            "3": "Saisir un nouveau joueur",
            "4": "Ajouter un joueur au tournoi",
            "5": "Débuter ou continuer un tour",
            "7" : "Lister tous les joueurs",
            "9": "Lister tous les joueurs du tournoi",
            "10": "Lister les tours et les matches du tour",
            "11": "Retour au menu principal",
            "12": "Quitter"
        },
        "input": "None",
        "input_choice": "Entrez le numéro de votre choix : "
    },
    # Menu lorsqu'un tournoi et un tour sont démarrés
    "002": {
        "title": None,
        "content": None,
        "actions": {
            "6": "Saisir un résultat",
            "7" : "Lister tous les joueurs",
            "9": "Lister tous les joueurs du tournoi",
            "10": "Lister les tours et les matches du tour",
            "11": "Retour au menu principal",
            "12": "Quitter"
        },
        "input": "None",
        "input_choice": "Entrez le numéro de votre choix : "
    },
    # Saisir le nom d'un tournoi
    "10" : {
        "title" : "SAISIR UN NOUVEAU TOURNOI 1/2",
        "content": None,
        "actions": None,
        "input": "Entrez le nom du tournoi : ",
        "input_choice" : None
    },
    # Saisir le lieu d'un tournoi
    "11": {
        "title": "SAISIR UN NOUVEAU TOURNOI 2/2",
        "content": None,
        "actions": None,
        "input": "Entrez le lieu du tournoi : ",
        "input_choice" : None
    },
    # Choisir un tournoi à démarrer
    "20": {
        "title": "DEMARRER UN TOURNOI",
        "content": None,
        "actions": None,
        "input": None,
        "input_choice" : "Entrez le numéro de votre choix : "
    },
    # Saisir le nom d'un joueur
    "30": {
        "title": "SAISIR UN NOUVEAU JOUEUR 1/2",
        "content": None,
        "actions": None,
        "input": "Entrez le nom du joueur : ",
        "input_choice": None
    },
    # Donner des critères de recherche d'un joueur
    "40": {
        "title": "AJOUTER UN JOUEUR AU TOURNOI 1/2",
        "content": None,
        "actions": None,
        "input": "Entrez le nom ou une partie du nom du jouer (tapez *** pour lister tout les joueurs) : ",
        "input_choice" : None
    },
    # Choisir un joueur pour l'ajouter au tournoi
    "41": {
        "title": "AJOUTER UN JOUEUR AU TOURNOI 2/2",
        "content": None,
        "actions": None,
        "input": None,
        "input_choice" : "Entrez le numéro de votre choix : "
    },
    # Obtenir une confirmation de l'utilisateur
    "50": {
        "title": "DEMANDE DE VALIDATION",
        "content": None,
        "actions": None,
        "input": "Pour valider tapez Y ou y : ",
        "input_choice" : None
    },
    # Lister les tours et les matches du tour
    "100": {
        "title": "TOUR ET MATCHES DU TOUR",
        "content": None,
        "actions": None,
        "input": "Validez pour continuer.",
        "input_choice": None
    }
}
