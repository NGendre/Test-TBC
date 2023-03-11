# INFOS
python version: 3.10
required packages : django, pandas, requests, pygsheets, numpy
USE: pip install django pandas requests pygsheets numpy

# URL utiles
liste des url utilisées (sur postman):
https://api.postman.com/collections/26301474-81deb685-867f-4a4e-ab9b-6ef31d0d504d?access_key=PMAT-01GV8MZTBWAWBGZ6DQPA6Z028J
url du tableau gsheets:
https://docs.google.com/spreadsheets/d/1wBQ3AvJ5r3_CJMb7cEc2MIdpPYF9iRiDfdlWdf_fb7s/edit#gid=0

# Fonctionnement

Architecture :
 - coucou
 
Fonctionnement : 
 - lancer la commande `python manage.py runserver` dans la racine du projet après avoir installé les packages nécessaires

Hébergement et déploiement:
- N'ayant aucune experience concernant le domaine, je ne sais pas comment pouvoir 

# Cahier des charges

Backend OMDB avec (NodeJS + Typescript) ou Python:
- Créer un projet capable de recevoir/répondre à des requêtes web, 
- Faire des appels à l'API http://www.omdbapi.com/ et récupérer un listing des films (Image, Titre, Année, Réalisateur).
- Mettre à disposition la liste des films "Fast & Furious" au format JSON dans notre serveur web via l'url /films
- Créer une URL qui va récupérer la liste des films "Pirates des caraïbes" et qui va les stocker dans un Google Spreadsheet en ligne 

Ajouter dans le Spreadsheet et dans le retour de l'API, les propriétés suivantes:
- Un propriété de type boolean pour indiquer si le film a été produit avant 2015
- Un propriété de type boolean pour indiquer si Paul Walker est un des acteurs du film
- Un propriété qui liste les acteurs en commun avec les films Star-Wars 
- Ajouter une sécurité simple permettant d'éviter les accès Anonymes à cette API 

Expliquer en quelques phrases (README):
- Comment il est construit ?
- Comment faire fonctionner le projet ?
- Comment tu envisages la partie hébergement ?
- Comment tu vois une éventuelle montée en charge du système ?
- Ses forces, faiblesses, NEXT STEPS pour la mise en prod.
