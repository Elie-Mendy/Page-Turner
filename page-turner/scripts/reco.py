#!/usr/bin/python
# -- coding: utf-8 --

# Importation des bibliothèques nécessaires
import os
import sys
import re
import nltk
import warnings
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from IPython.display import display  # affiche proprement ma table pivot
from nltk.corpus import stopwords

# modèle pour la tokénisation des textes -- utiles pour "content_based_recommender2()"
nltk.download("stopwords")
nltk.download("punkt")

# desactivation des logs de warning
warnings.filterwarnings("ignore")

# Chargement du datasets
df = pd.read_csv(os.path.join(sys.argv[2], "scripts/Preprocessed_data.csv"))
rating_counts = pd.DataFrame(df["book_title"].value_counts())

# rare books are excluded from the recommendation
rare_books = rating_counts[rating_counts["count"] <= 10].index

###::::::::::::::::::::::::::::::::::::::::::::::::: FONCTIONS :::::::::::::::::::::::::::::::###


def get_isbn(book_title: str) -> str:
    """return the isbn of a book from its title

    Args:
        book_title (str): the title of the book

    Returns:
        str: the isbn of the book
    """
    return df.loc[df["book_title"] == book_title].iloc[0][1]


def get_book_title(searchValue: str) -> str:
    """return the title of a book from a search value

    Args:
        searchValue (str): the search value

    Returns:
        str: the title of the book
    """
    books = df[df["book_title"].str.contains(searchValue)].sort_values(
        "rating", ascending=True
    )
    for title in books["book_title"].values:
        if title not in rare_books:
            return title

    print("❌ COULD NOT FIND ❌")


def content_based(bookTitle) -> None:
    """return the recommended books from a book title

    Args:
        bookTitle (str): the title of the book

    Returns:
        None: print the recommended books isbns
    """
    bookTitle = get_book_title(bookTitle)

    # if the book is not found
    if not bookTitle:
        return

    # select and process common books
    common_books = df[~df["book_title"].isin(rare_books)]
    common_books = common_books.drop_duplicates(subset=["book_title"])
    common_books.reset_index(inplace=True)
    common_books["index"] = [i for i in range(common_books.shape[0])]

    # targetet colomns
    targets = ["book_title", "book_author", "publisher", "Category"]

    # create a new column with all the features
    common_books["all_features"] = [
        " ".join(common_books[targets].iloc[i,].values)
        for i in range(common_books[targets].shape[0])
    ]

    # get the index of the book
    index = common_books[common_books["book_title"] == bookTitle]["index"].values[0]

    # vectorize the data
    vectorizer = CountVectorizer()
    common_booksVector = vectorizer.fit_transform(common_books["all_features"])

    # compute the similarity
    similarity = cosine_similarity(common_booksVector)

    # get the similar books
    similar_books = list(enumerate(similarity[index]))
    similar_booksSorted = sorted(similar_books, key=lambda x: x[1], reverse=True)[1:40]

    # print the recommended books
    recommended_books = []
    for i in range(len(similar_booksSorted)):
        recommended_books.append(
            common_books[common_books["index"] == similar_booksSorted[i][0]][
                "book_title"
            ].item()
        )
    print(", ".join([get_isbn(book_title) for book_title in recommended_books]))


####:::::::::::::::::::::::::::::::::::::::::: RECOMMANDATIONS :::::::::::::::::::::::::::::::::::::###


if __name__ == "__main__":
    searchValue = sys.argv[1].lower()
    content_based(searchValue)
