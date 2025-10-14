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

Installer le paquet "flake8-formatter-junit-xml" qui permet de convertir le rapport standard de Flake8 en un format junit-xml :

**pip install flake8-formatter-junit-xml**

Installer le paquet "junit2html" qui epermet de convertir les fichiers de rapport JUnit XML en un rapport visuel lisible au format HTML :

**pip install junit2html**

Exécuter la commande suivante pour générer le rapport flake8 au format junit-xml :

**flake8 --output-file=flake8_report.xml --format=junit-xml**

Exécuter la commande suivant pour convertir le fichier xml obtenu au format HTML :

**junit2html flake8_report.xml flake8_report.html**
