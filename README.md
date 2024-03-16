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

[Lien vers la vidéo](https://www.loom.com/share/47c686208f584b0da183639bb867d732?sid=f943df3d-9e22-4272-ab80-099e152ceef8)

## Installation et lancement du projet

### Image Docker
```bash
docker pull emstud/page-turner:v1.0.1
docker run -d --name page-turner -p 8000:8000 emstud/page-turner:v1.0.1


# for starting / stopping the app later
docker stop page-turner
docker start page-turner
```

### Repository git 
```sh
# clone du repository en local
git clone https://github.com/Elie-Mendy/Page-Turner.git
TODO - add installation steps 
```

```sh

# création de l'environnement virtuel 
python3 -m venv .env

# activaton de l'environnement virtuel
source ./env/bin/activate

# installation des dépendences
pip install -r requirements.txt

# sinon lancer l'installation des packets manuellement :
pip install --upgrade pip
pip install django
pip install djangorestframework
pip install python-dotenv
pip install django-cors-headers
pip install psycopg2-binary
pip install djangorestframework-simplejwt
pip install numpy
pip install tensorflow
pip install pandas
pip install scikit-learn
pip install nltk
pip install matplotlib
pip install ipython

# lancement de l'application
cd page-turner
python3 manage.py runserver
```

### Connexion a l'application
L'Application sera accessible en local sur le port 8000 : *`http://localhost:8000`*

**Administrateur par Defaut:** 
identifiant : *admin@example.com*
mot de passe : *test123*

## Documentation

TODO - add docs to project

___

## Technologies utilisées

### BackEnd:

#### Conteneurisation
 - [Docker](https://www.docker.com)

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


###### Réalisé par 
[Florine-Mendy](https://github.com/florine-mendy) 
[Elie-Mendy](https://github.com/Elie-Mendy) 
