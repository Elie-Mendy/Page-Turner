#!/usr/bin/python
# -- coding: utf-8 --

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import os
import sys
import re
import nltk
import requests
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display  # affiche proprement ma table pivot


from nltk.corpus import stopwords
nltk.download("stopwords")
# modèle pour la tokénisation des textes -- utiles pour "content_based_recommender2()"
nltk.download('punkt')


warnings.filterwarnings('ignore')

books = pd.read_csv(os.path.join(os.getcwd(), 'scripts/Preprocessed_data.csv'))

# copie le DataFrame books
df = books.copy()

# supprime les lignes qui contiennent des valeurs manquantes 'NaN'
df.dropna(inplace=True)

# réinitialise l'index du DataFrame après la suppression des lignes.
df.reset_index(drop=True, inplace=True)

# supprime les colonnes non nécessaires
df.drop(columns=['Unnamed: 0', 'location',
                 'img_s', 'img_m', 'city', 'age',
                 'state', 'Language', 'country',
                 'year_of_publication'], axis=1, inplace=True)

# nettoie la colonne 'Category'
df.drop(index=df[df['Category'] == '9'].index, inplace=True)
df['Category'] = df['Category'].apply(
    lambda x: re.sub('[\W_]+', ' ', x).strip())

# nettoie la colonne 'rating'
df.drop(index=df[df['rating'] == 0].index, inplace=True)


def get_isbn(book_title):
    return df.loc[df['book_title'] == book_title].iloc[0][1]


def custom_recommender(book_title):

    # ITEM-BASED
    book_title = str(book_title)
    if book_title in df['book_title'].values:
        rating_counts = pd.DataFrame(df['book_title'].value_counts())
        rare_books = rating_counts[rating_counts['count'] <= 180].index
        common_books = df[~df['book_title'].isin(rare_books)]

        if book_title in rare_books:
            random = pd.Series(
                common_books['book_title'].unique()).sample(2).values
            print('There are no recommendations for this book')
            print('Try: \n')
            print('{}'.format(random[0]), '\n')
            print('{}'.format(random[1]), '\n')

        else:
            ##### --------------------------------- VECTORISATION ET CALCUL SIMILARITE ----------------------#####
            user_book_df = common_books.pivot_table(
                index=['user_id'], columns=['book_title'], values='rating')

            book = user_book_df[book_title]
            recom_data = pd.DataFrame(user_book_df.corrwith(
                book).sort_values(ascending=False)).reset_index(drop=False)

            if book_title in [book for book in recom_data['book_title']]:
                recom_data = recom_data.drop(
                    recom_data[recom_data['book_title'] == book_title].index[0])

            low_rating = []
            for i in recom_data['book_title']:
                if df[df['book_title'] == i]['rating'].mean() < 5:
                    low_rating.append(i)

            if recom_data.shape[0] - len(low_rating) > 5:
                recom_data = recom_data[~recom_data['book_title'].isin(
                    low_rating)]

            recom_data = recom_data[0:10]
            recom_data.columns = ['book_title', 'corr']
            recommended_books = []
            for i in recom_data['book_title']:
                recommended_books.append(i)

            df_new = df[~df['book_title'].isin(recommended_books)]

            # CONTENT-BASED (Title, Author, Publisher, Category)
            rating_counts = pd.DataFrame(df_new['book_title'].value_counts())

            # rare_books = rating_counts[rating_counts['book_title'] <= 100].index
            rare_books = rating_counts[rating_counts['count'] <= 100].index

            common_books = df_new[~df_new['book_title'].isin(rare_books)]
            common_books = common_books.drop_duplicates(subset=['book_title'])
            common_books.reset_index(inplace=True)
            common_books['index'] = [i for i in range(common_books.shape[0])]
            target_cols = ['book_title',
                           'book_author', 'publisher', 'Category']
            common_books['combined_features'] = [' '.join(
                common_books[target_cols].iloc[i,].values) for i in range(common_books[target_cols].shape[0])]
            cv = CountVectorizer()
            count_matrix = cv.fit_transform(common_books['combined_features'])
            cosine_sim = cosine_similarity(count_matrix)
            index = common_books[common_books['book_title']
                                 == book_title]['index'].values[0]
            sim_books = list(enumerate(cosine_sim[index]))
            sorted_sim_books = sorted(
                sim_books, key=lambda x: x[1], reverse=True)[1:10]

            books = []
            for i in range(len(sorted_sim_books)):
                books.append(
                    common_books[common_books['index'] == sorted_sim_books[i][0]]['book_title'].item())

            for i in books:
                recommended_books.append(i)

            df_new = df_new[~df_new['book_title'].isin(recommended_books)]

            # CONTENT-BASED (SUMMARY)
            rating_counts = pd.DataFrame(df_new['book_title'].value_counts())
            # rare_books = rating_counts[rating_counts['book_title'] <= 100].index
            rare_books = rating_counts[rating_counts['count'] <= 100].index

            common_books = df_new[~df_new['book_title'].isin(rare_books)]

            common_books = common_books.drop_duplicates(subset=['book_title'])
            common_books.reset_index(inplace=True)
            common_books['index'] = [i for i in range(common_books.shape[0])]

            summary_filtered = []
            for i in common_books['Summary']:
                i = re.sub("[^a-zA-Z]", " ", i).lower()
                i = nltk.word_tokenize(i)
                i = [word for word in i if not word in set(
                    stopwords.words("english"))]
                i = " ".join(i)
                summary_filtered.append(i)

            common_books['Summary'] = summary_filtered
            cv = CountVectorizer()
            count_matrix = cv.fit_transform(common_books['Summary'])
            cosine_sim = cosine_similarity(count_matrix)
            index = common_books[common_books['book_title']
                                 == book_title]['index'].values[0]
            sim_books = list(enumerate(cosine_sim[index]))
            sorted_sim_books2 = sorted(
                sim_books, key=lambda x: x[1], reverse=True)[1:10]
            sorted_sim_books = sorted_sim_books2[:10]
            summary_books = []
            for i in range(len(sorted_sim_books)):
                summary_books.append(
                    common_books[common_books['index'] == sorted_sim_books[i][0]]['book_title'].item())

            for i in summary_books:
                recommended_books.append(i)

            df_new = df_new[~df_new['book_title'].isin(recommended_books)]

            # TOP RATED OF CATEGORY
            category = common_books[common_books['book_title']
                                    == book_title]['Category'].values[0]
            top_rated = common_books[common_books['Category'] == category].groupby(
                'book_title').agg({'rating': 'mean'}).reset_index()

            if top_rated.shape[0] == 1:
                recommended_books.append(
                    common_books[common_books['index'] == sorted_sim_books2[2][0]]['book_title'].item())
            ##### --------------------------------- VECTORISATION ET CALCUL SIMILARITE ----------------------#####

            ##### --------------------------------- FORMATE AFFICHAGE RESULTAT ------------------------------#####
            else:
                top_rated.drop(
                    top_rated[top_rated['book_title'] == book_title].index[0], inplace=True)
                top_rated = top_rated.sort_values(
                    'rating', ascending=False).iloc[:1]['book_title'].values[0]
                recommended_books.append(top_rated)

            print(', '.join([get_isbn(book_title)
                  for book_title in recommended_books]))

        ##### --------------------------------- FORMATE AFFICHAGE RESULTAT ------------------------------#####
    else:
        print('Cant find book in dataset, please check spelling')


if __name__ == "__main__":
    book_title = sys.argv[1]
    # The Summons
    custom_recommender(book_title)
