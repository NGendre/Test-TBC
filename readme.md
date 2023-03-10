# INFOS
python version: 3.10

required packages : django, pandas, requests, pygsheets, numpy

USE: `pip install django pandas requests pygsheets numpy`

Je n'ai pqs réussi a faire fonctionner la sécurité sur les endpoints, mais mes progrès sont sur la branche `authentication`.

# URL utiles
Liste des url utilisées (sur postman):
https://api.postman.com/collections/26301474-81deb685-867f-4a4e-ab9b-6ef31d0d504d?access_key=PMAT-01GV8MZTBWAWBGZ6DQPA6Z028J

Url du tableau gsheets:
https://docs.google.com/spreadsheets/d/1wBQ3AvJ5r3_CJMb7cEc2MIdpPYF9iRiDfdlWdf_fb7s/edit#gid=0

# Explications demandées

## Construction: 

3 couches:
- Couche "url": contient la liste des url accessibles et indique quelles méthodes seront appelées
- Couche "view": contient les methodes transmettant les données a l'utilisateur
- Couche "service": contient les méthodes faisant appel aux différentes api et faisant le traitement de données

Directories:
- Films: contient le controller et les vues pour les endpoints /films
- Resources: contient la clé json permettant d'envoyer des données a l'api google
- Services: contient les services faisant des appels aux api et les méthodes de traitement de données
- Test_TBC: fichiers de configuration de l'application

## Fonctionnement

- Installer les packages python suivants: django, pandas, requests, pygsheets, numpy
- Lancer la commande `python manage.py runserver` dans la racine du projet après avoir installé les packages nécessaires

## Hébergement

N'ayant aucune experience concernant le domaine et n'ayant pas trouvé de ressources m'aidant à le faire fonctionner, je ne sais pas comment préparer le déploiement en production.

## Scaling

- Améliorer la separation des couches, ce qui permettrait de simplifier le développement
- Trouver une API permettant des appels plus spécifiques pour éviter de faire trop d'appels externes

## Forces/faiblesses

### Forces

- Effectue les besoins demandés
- Renvoie précisement la liste des films demandés

### Faiblesses

- Pas de sécurité sur les url
- Beaucoup d'appels api
- Données en dur dans le code

## Mise en prod

- Implémenter un entrypoint pour autoriser le trafic http
- Ajouter un fichier de requirements listant les packages dont l'appli a besoin


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
