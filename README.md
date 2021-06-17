# 1. Projet 13 - aroma project (branche master)

lien https://aromaproject-maximilien.herokuapp.com/

Réalisation d'une application qui permet de trouver des conseils en
aromathérapie selon la pathologie selectionnée


## 2. Ressources extérieures utilisées :
Livre : "le guide terre vivante des huiles essentielles"
écrit par Françoise Couic Marinier et Maximilien Lehoux

## 3. Outils
Environnement virtuel
Développement en python 3.7,
Base de données PostgreSQL 13.0,
Gestion des templates et des tables avec Django 3.1,
Design avec Bootstrap 4.

## 4. Installation des dépendances
"""
pip install -r requirements.txt
"""

## 5. Tests
Lancer les tests :
"""
manage.py test
"""

## 6. Lancement en local
Créer et remplir la base de données :
(utilisation de postgreSQL, modifiez-vos donnée serveur dans le fichier setting )


Commande de lancement =
"""
manage.py migrate
manage.py makemigrations
"""

Remplir base de donnée
"""
via le site administrateur de django
"""

Lancer l'application :
"""
python manage.py runserver
"""