required packages: django,pandas,requests,pygsheets

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
