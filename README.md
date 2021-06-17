# 1. Projet 13 - aroma project (branche master)

lien https://aromaproject-maximilien.herokuapp.com/

R�alisation d'une application qui permet de trouver des conseils en
aromath�rapie selon la pathologie selectionn�e


## 2. Ressources ext�rieures utilis�es :
Livre : "le guide terre vivante des huiles essentielles"
�crit par Fran�oise Couic Marinier et Maximilien Lehoux

## 3. Outils
Environnement virtuel
D�veloppement en python 3.7,
Base de donn�es PostgreSQL 13.0,
Gestion des templates et des tables avec Django 3.1,
Design avec Bootstrap 4.

## 4. Installation des d�pendances
"""
pip install -r requirements.txt
"""

## 5. Tests
Lancer les tests :
"""
manage.py test
"""

## 6. Lancement en local
Cr�er et remplir la base de donn�es :
(utilisation de postgreSQL, modifiez-vos donn�e serveur dans le fichier setting )


Commande de lancement =
"""
manage.py migrate
manage.py makemigrations
"""

Remplir base de donn�e
"""
via le site administrateur de django
"""

Lancer l'application :
"""
python manage.py runserver
"""