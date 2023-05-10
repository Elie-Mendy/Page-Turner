#!/usr/bin/python
# -- coding: utf-8 --

import os
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
import re
from PIL import Image
import requests
import random
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords


# ouverture des dataset
books=pd.read_csv(os.path.join(os.getcwd(), "scripts/Books.csv"))
ratings=pd.read_csv(os.path.join(os.getcwd(), "scripts/Ratings.csv"))
users=pd.read_csv(os.path.join(os.getcwd(), "scripts/Users.csv"))












"""------------------------------------------------------------ PREPROCESSING -------------------------------------------------------"""
books_data=books.merge(ratings,on="ISBN") # nouveau dataframe : combine les données des datasets "books" et "ratings" en fonction de leur colonne commune "ISBN"
df=books_data.copy() # on travaille sur une copie de books_data
df.dropna(inplace=True) # supprime toutes les lignes contenant des valeurs NaN 
df.drop(index=df[df["Book-Rating"]==0].index,inplace=True) # supprime toutes les lignes contenant des valeurs 0 dans la col Book-Rating
df.reset_index(drop=True,inplace=True) # màj des index
df.drop(columns=["Year-Of-Publication","Image-URL-S","Image-URL-M"],axis=1,inplace=True) # suppression des col inutiles
df["Book-Title"]=df["Book-Title"].apply(lambda x: re.sub("[\W_]+"," ",x).strip()) # nettoie les titres des livres



def get_isbn(book_title) :
  return df.loc[df['Book-Title'] == book_title].iloc[0][0]




"""------------------------------------------------------------ PREAPARE CALCUL -------------------------------------------------------"""
new_df=df[df['User-ID'].map(df['User-ID'].value_counts()) > 200]  # Drop users who vote less than 200 times.
users_pivot=new_df.pivot_table(index=["User-ID"],columns=["Book-Title"],values="Book-Rating") # table pivot qui contient les évaluations des utilisateurs pour chaque livre.
users_pivot.fillna(0,inplace=True)

# Trouve les 5 livres préférés d'un utilisateur donné
def users_choice(id): 
  users_fav=new_df[new_df["User-ID"]==id].sort_values(["Book-Rating"],ascending=False)[0:5] #elle trie ces lignes par ordre décroissant de la note de livre (Book-Rating) et ne garde que les 5 premières lignes correspondantes aux 5 livres préférés de l'utilisateur
  return users_fav






"""------------------------------------------------------------ CALCUL SIMILARITES ENTRE UTILISATEURS ---------------------------------"""

# Recommande des livres à un utilisateur donné en fonction des préférences 
# d'utilisateurs similaires en utilisant la similarité cosinus. 
# Cette fonction prend l'ID de l'utilisateur comme entrée et renvoie 
# les cinq ID d'utilisateurs similaires, qui ont des préférences similaires.

def user_based(new_df,id):
  # l'id de l'utilisateur est-il présent dans le dataframe ?
  if id not in new_df["User-ID"].values:
    print("❌ User NOT FOUND ❌")
      
      
  else:
    # oui, alors cherche son index le tableau croisé/table pivot qui contient les évaluations de tous les utilisateurs pour tous les livres.
    index=np.where(users_pivot.index==id)[0][0]

    """ Elle calcule ensuite la similarité de cosinus entre les évaluations de 
    tous les utilisateurs pour tous les livres à l'aide de la fonction 
    "cosine_similarity" de la bibliothèque "sklearn". La variable "similarity" 
    est une matrice carrée de dimensions "n x n" où "n" est le nombre total 
    d'utilisateurs dans le DataFrame "new_df". La case (i, j) de la matrice 
    "similarity" contient la similarité de cosinus entre les évaluations 
    des utilisateurs i et j pour tous les livres.
    """
    similarity=cosine_similarity(users_pivot)
    similar_users=list(enumerate(similarity[index]))
    similar_users = sorted(similar_users,key = lambda x:x[1],reverse=True)[0:5] # contient les 5 indices des utilisateurs les plus similaires à l'utilisateur, triés par ordre décroissant de similarité.
    user_rec=[] # contiendra les identifiants des 5 utilisateurs similaires
  
    """
    Pour chaque utilisateur similaire, la fonction récupère toutes les 
    évaluations de ce dernier dans le DataFrame "new_df", puis elle ajoute 
    l'identifiant de l'utilisateur dans la liste "user_rec". Ainsi, à la fin 
    de la boucle, la liste "user_rec" contient les identifiants de tous les 
    utilisateurs similaires à l'utilisateur
    """
    for i in similar_users:
      data=df[df["User-ID"]==users_pivot.index[i[0]]]
      user_rec.extend(list(data.drop_duplicates("User-ID")["User-ID"].values))
      
  return user_rec








"""------------------------------------------------------------ SELECTION DES RECOMMANDATIONS ------------------------------------------"""

# La fonction renvoie les 5 premiers titres des livres recommandés pour l'utilisateur

# recommander des livres à un utilisateur donné en fonction des préférences 
# de ces cinq utilisateurs similaires. Cette fonction prend l'ensemble d'ID 
# d'utilisateurs similaires et l'ID de l'utilisateur cible et renvoie les 
# cinq livres recommandés.


# "new_df" -- contient les données de l'ensemble des utilisateurs et des livres qu'ils ont évalués.
# "user" est une liste de "Book-Title" de livres recommandés par d'autres utilisateurs similaires.
# "user_id" est l'ID de l'utilisateur pour lequel nous voulons trouver des recommandations
def common(new_df,user,user_id):
  x=new_df[new_df["User-ID"]==user_id] # stocke toutes les évaluations faites par l'utilisateur

  recommend_books=[] # stockera les recommandations de livres
  user=list(user)
  for i in user:
    y=new_df[(new_df["User-ID"]==i)] # 
    books=y.loc[~y["Book-Title"].isin(x["Book-Title"]),:] # 
    books=books.sort_values(["Book-Rating"],ascending=False)[0:5]
    recommend_books.extend(books["Book-Title"].values)
      
  return recommend_books[0:5]













"""------------------------------------------------------------ FORMATE AFFICHAGE RESULTATS ------------------------------------------"""

# Selectionne un utilisateur au hasard et affiche ces 5 livres péférés ainsi que les cinq  livres qui lui sont recommandés

# user_id=random.choice(new_df["User-ID"].values)
# user_choice_df=pd.DataFrame(users_choice(user_id))
# user_favorite=users_choice(user_id)
# n=len(user_choice_df["Book-Title"].values)
# print("🟦 USER: {} ".format(user_id))
    
# fig,ax=plt.subplots(1,n,figsize=(17,5))
# fig.suptitle("YOUR FAVORITE BOOKS",fontsize=40,color="salmon")
    
# for i in range(n):
#   url=new_df.loc[new_df["Book-Title"]==user_choice_df["Book-Title"].tolist()[i],"Image-URL-L"][:1].values[0]
#   #img=Image.open(requests.get(url,stream=True).raw)
#   #ax[i].imshow(img)
#   ax[i].axis("off")
#   ax[i].set_title("RATING: {} ".format(round(new_df[new_df["Book-Title"]==user_choice_df["Book-Title"].tolist()[i]]["Book-Rating"].mean(),1)),y=-0.20,color="mediumorchid",fontsize=22)
#   ax[i].text(0.5,-0.4,user_choice_df["Book-Title"].tolist()[i],horizontalalignment='center',fontsize=10) # affiche le titre du livre 
#   fig.show()

# user_based_rec=user_based(new_df,user_id)
# books_for_user=common(new_df,user_based_rec,user_id)
# books_for_userDF=pd.DataFrame(books_for_user,columns=["Book-Title"])

# fig,ax=plt.subplots(1,5,figsize=(17,5))
# fig.suptitle("YOU MAY ALSO LIKE THESE BOOKS",fontsize=40,color="mediumseagreen")
# for i in range(5):
#   url=new_df.loc[new_df["Book-Title"]==books_for_userDF["Book-Title"].tolist()[i],"Image-URL-L"][:1].values[0]
#   #img=Image.open(requests.get(url,stream=True).raw)
#   #ax[i].imshow(img)
#   ax[i].axis("off")
#   ax[i].set_title("RATING: {} ".format(round(new_df[new_df["Book-Title"]==books_for_userDF["Book-Title"].tolist()[i]]["Book-Rating"].mean(),1)),y=-0.20,color="mediumorchid",fontsize=22)
#   ax[i].text(0.5,-0.4,user_choice_df["Book-Title"].tolist()[i],horizontalalignment='center',fontsize=10) # affiche le titre du livre 
#   fig.show()




if __name__ == "__main__" :
  user_id=random.choice(new_df["User-ID"].values)
  user_choice_df=pd.DataFrame(users_choice(user_id))
  user_favorite=users_choice(user_id)
  n=len(user_choice_df["Book-Title"].values)



  print("🟦 USER: {} ".format(user_id))
  print("\n\nYOUR FAVORITE BOOKS\n")
  # ajout flo
  user_fav_booklist = user_choice_df["Book-Title"].values
  for book_title in (user_fav_booklist) :
    print([get_isbn(book_title) for book_title in user_fav_booklist])


  user_based_rec=user_based(new_df,user_id)
  books_for_user=common(new_df,user_based_rec,user_id)
  books_for_userDF=pd.DataFrame(books_for_user,columns=["Book-Title"])


  print("\n\nYOU MAY ALSO LIKE THESE BOOKS\n")
  # ajout flo 
  reco = books_for_userDF["Book-Title"].tolist()
  for book_title in (reco) :
    print([get_isbn(book_title) for book_title in reco])