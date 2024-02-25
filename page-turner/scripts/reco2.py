#!/usr/bin/python
# -- coding: utf-8 --


# Importation des bibliothèques nécessaires
import os
import sys
import warnings
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import re

# Suppression des avertissements
warnings.filterwarnings("ignore")

# Chargement des datasets
books = pd.read_csv(os.path.join(sys.argv[2], "scripts/Books.csv"))
ratings = pd.read_csv(os.path.join(sys.argv[2], "scripts/Ratings.csv"))
users = pd.read_csv(os.path.join(sys.argv[2], "scripts/Users.csv"))



###::::::::::::::::::::::::::::::::::::::::::::::::: FONCTIONS :::::::::::::::::::::::::::::::###


def get_isbn(book_title):
    """
    Récupère l'ISBN d'un livre à partir de son titre.
    
    Args:
    - book_title (str): Le titre du livre.
    
    Returns:
    - str: L'ISBN du livre.
    """
    return df.loc[df['Book-Title'] == book_title].iloc[0][0]


def get_favourite_books_isbn(user_id):
    """
    Renvoie les isbns des 4 livres préférés d'un utilisateur.
    
    Args:
    - user_id (int): L'ID de l'utilisateur.
    
    Returns:
    - List[str]: Les isbns des 4 livres préférés de l'utilisateur.
    """
    df_favorite_books = new_df[new_df["User-ID"] == user_id].sort_values(["Book-Rating"], ascending=False).head(4) 
    # conversion des isbn pour retourner une liste d'entiers
    return df_favorite_books["ISBN"].tolist()


def get_similar_users(new_df, user_id):
    """
    Identifie les utilisateurs ayant des goûts similaires à un utilisateur donné en utilisant la similarité cosinus.
    
    Args:
    - new_df (DataFrame): Le dataframe contenant les données des utilisateurs et leurs évaluations.
    - user_id (int): L'ID de l'utilisateur cible.
    
    Returns:
    - list[int]: Liste des ID des utilisateurs similaires.
    """
    user_ids = []
    if user_id not in new_df["User-ID"].values:
        print("❌ User NOT FOUND ❌")
    else:
        index = np.where(users_pivot.index == user_id)[0][0]
        similarity = cosine_similarity(users_pivot)
        similar_users = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)[0:5]
        for id in similar_users:
            data = df[df["User-ID"] == users_pivot.index[id[0]]]
            user_ids.extend(list(data.drop_duplicates("User-ID")["User-ID"].values))
    return user_ids


def get_recommanded_books(new_df, user_ids, user_id):
    """
    Recommande des livres à un utilisateur basé sur les préférences d'utilisateurs similaires.
    
    Args:
    - new_df (DataFrame): Le dataframe contenant les données des utilisateurs et leurs évaluations.
    - user_ids (list): Liste des ID des utilisateurs similaires.
    - user_id (int): L'ID de l'utilisateur cible.
    
    Returns:
    - list: Liste des isbn des livres recommandés.
    """
    recommended_books = []
    user_ids = list(user_ids)
    # récupération des livres évalués par l'utilisateur
    user_favorite_books = new_df[new_df["User-ID"] == user_id]
    # récupération des livres évalués par les utilisateurs similaires
    for id in user_ids:
        # récupération des livres évalués par l'utilisateur
        books = new_df[(new_df["User-ID"] == id)]
        # suppression des doublons
        books = books.loc[~books["Book-Title"].isin(user_favorite_books["Book-Title"]), :]
        # tri par note décroissante et récupération des 10 premiers livres
        books = books.sort_values(["Book-Rating"], ascending=False)[0:10]
        # ajout des livres à la liste des livres recommandés
        recommended_books.extend(books["Book-Title"].values)
    return [get_isbn(book_title) for book_title in recommended_books[0:50]]



###::::::::::::::::::::::::::::::::::::::::::::::PRÉTRAITEMENT DES DONNÉES :::::::::::::::::::::::::::::::::###


# Fusion des datasets books et ratings sur la colonne ISBN
books_data = books.merge(ratings, on="ISBN")
df = books_data.copy()  # Création d'une copie pour travailler dessus

# Nettoyage des données
df.dropna(inplace=True)  # Suppression des lignes avec des valeurs NaN
df.drop(index=df[df["Book-Rating"] == 0].index, inplace=True)  # Suppression des évaluations égales à 0
df.reset_index(drop=True, inplace=True)  # Réinitialisation des index
df.drop(columns=["Year-Of-Publication", "Image-URL-S", "Image-URL-M"], axis=1, inplace=True)  # Suppression des colonnes inutiles
df["Book-Title"] = df["Book-Title"].apply(lambda x: re.sub("[\W_]+", " ", x).strip())  # Nettoyage des titres des livres



###::::::::::::::::::::::::::::::::::::::::::: PRÉPARATION POUR LE CALCUL :::::::::::::::::::::::::::::::::::###


# Filtrage sur les utilisateurs ayant évalué plus de 200 livres
new_df = df[df['User-ID'].map(df['User-ID'].value_counts()) > 200]

# Création d'une table pivot des évaluations des utilisateurs
users_pivot = new_df.pivot_table(index=["User-ID"], columns=["Book-Title"], values="Book-Rating")
users_pivot.fillna(0, inplace=True)



####:::::::::::::::::::::::::::::::::::::::::: RECOMMANDATIONS ::::::::::::::::::::::::::::::::::::::::::::::::###


if __name__ == "__main__":
    # récupération du user_id donnée en argument du script
    user_id = np.int64(sys.argv[1])

    # récupération des isbns des 4 livres préférés de l'utilisateur
    favourite_books_isbn = get_favourite_books_isbn(user_id)
    
    # récupération de 5 utilisateurs similaires
    similar_users = get_similar_users(new_df, user_id)

    # recomandation de livres
    recommanded_books = get_recommanded_books(new_df, similar_users, user_id)

    # formatage de la valeur de retour 
    print(', '.join(favourite_books_isbn + recommanded_books))
