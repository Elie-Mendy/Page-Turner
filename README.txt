# Page Turner

## Présentation générale

Le projet Page Turner présenté dans ce repository est un proof of concept pour une plateforme Web caumunautaire proposant au des lecteurs les fonctionalétées suivantes :
* Connexion sécurisée à la plateforme 
* Création / Edition de profil utilisateur
* Algorithmes de recommandations de livre
  * 1) sur la base de leurs préférences et gouts de lectures
  * 2) sur la base de raprochement entre profils similaires de lecteurs  
* Ajout de commentaires sur les livres lus
* Moderation des commentaires toxiques au moyen d'un modèle de Machine Learning

A l'avenir, plusieures fonctionalités seront implémentés 
* Création / Edition de challenges de lectures 
* Création / Editionde lectures communes.
* Messagerie instantanée.

## Video Présentation

[Lien vers la vidéo](https://www.loom.com/share/14d65c3a354f40b386325679b59a8bd1)


## Installation du projet
```sh
git clone https://github.com/Elie-Mendy/Page-Turner.git
TODO - add installation steps 
```

## Lancement l'application

### Backend
```sh
source ./env/bin/activate
cd backend
python3 manage.py runserver
```

### Frontend
```sh
cd frontend 
npm start
```
L'API backend sera accessible en local sur le port 8000 : `http://localhost:8000`
L'application sera accessible en local sur le port 3000 : `http://localhost:3000`


## Documentation
TODO - add docs to project

 
___

## Technologies utilisées

### BackEnd:
#### API
 - [Python3](https://www.python.org)
 - [pip](https://pypi.org/project/pip/)
 - [Django](https://www.djangoproject.com)
 - [Django-Rest-Framework](https://www.django-rest-framework.org)

#### Data
 - [pandas]
 - [numpy]
 - [tensorflow]
 - [keras]

### FrontEnd:
 - [React](https://fr.legacy.reactjs.org)
 - [Bootstrap5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
 - [Redux](https://redux.js.org)
  
___

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.


###### Realised by 
[Florine-Mendy](https://github.com/florine-mendy) 
[Elie-Mendy](https://github.com/Elie-Mendy) 
