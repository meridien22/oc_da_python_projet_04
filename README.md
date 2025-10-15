## CHESS MASTER PRO ULTIMATE

CHESS MASTER PRO ULTIMATE est un programme qui permet de gérer des tournois d'échecs :

* Gestion des joueurs :
  * Saisi d'un nouveau joueur
  * Inscription d'un joueur dans un tournoi
* Gestion des tournois :
  * Génération des matchs en fonctions du classement des joueurs
  * Génération des tours en fonction du nombre de tours défini dans le tournoi
  * Saisi des résulats
* Edtition de rapport :
  * Liste de tous les joueurs de la fédaration
  * Liste de tous les jouers inscrits
  * Tableau du classement général du tournoi
  * Résumé des tours
  * Résumé des tournois
* Sauvegarde des données :
  * Sauvegarde des joueurs
  * Sauvegarde des tournois

## Comment exécuter le programme :

Il est préférable de créer un environnement virtuel pour exécuter le script.

Placer vous dans votre répertoire de travail et exécuter ces commandes :

**python -m venv env**

Activer ensuite votre environnement virtuel :

**env\Scripts\activate.bat** (Windows)

**source env/bin/activate** (Mac et Unix)

Pour finir installer les paquets nécessaires pour l'exécution du script :

**pip install -r requirements.txt**

Vous pouvez ensuite lancer le script :

**python main.py**

## Procédure pour générer un rapport flake8 du projet au format html :

Installer le paquet "flake8-html" qui permet de convertir le rapport standard de Flake8 en un format HTML :

**pip install flake8-html**

Exécuter ensuite la commande suivante pour générer le rapport flake8 au format HTML :

**flake8 --format=html --htmldir=flake_report**
