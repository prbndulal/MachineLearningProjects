import pandas as pd ## this library is used for data processing, csv files read I/O
import numpy as np ## this is used for linear algebra
from .helper import convert,convert3text,fetch_director,stem
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os
import joblib
import requests
import json

datapath='data'
movies=pd.read_csv(os.path.join(datapath,'tmdb_5000_movies.csv'))
credits=pd.read_csv(os.path.join(datapath,'tmdb_5000_credits.csv'))

#merge two dataset and assign to movies dataset

movies=movies.merge(credits, on='title')

# only select useful features for model creation
movies=movies[['movie_id','title','overview','genres','keywords','cast','crew']]

movies.dropna(inplace=True)
movies['genres']=movies['genres'].apply(convert)
movies['keywords']=movies['keywords'].apply(convert)
movies['cast']=movies['cast'].apply(convert3text)
movies['crew']=movies['crew'].apply(fetch_director)
movies['overview']=movies['overview'].apply(lambda x:x.split())
movies['genres']=movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords']=movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast']=movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew']=movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])
movies['tags']=movies['overview']+movies['genres']+movies['keywords']+movies['cast']+movies['crew']
movies_new_df=movies[['movie_id','title','tags']]
#print( movies_new_df['tags'][0])
movies_new_df['tags']=movies_new_df['tags'].apply( lambda x: " ".join(x)).apply(lambda x:x.lower()).apply(stem)
 

## CountVectorizer and Stop Words
cv=CountVectorizer(max_features=5000,stop_words='english')

vectors=cv.fit_transform(movies_new_df['tags']).toarray()


#cosine similarity 
similarity=cosine_similarity(vectors)
print (similarity)

def recommend(movie):
    movie_index=movies_new_df[movies_new_df['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=i[0]
        recommended_movies.append(movies_new_df.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters



def save_model(model,filename):
    model_dir="models"
    os.makedirs(model_dir,exist_ok=True) 
    filepath=os.path.join (model_dir,filename)
    joblib.dump(model,filepath)
    print('Saving model complete')

def fetch_poster(movie_id):
    url=f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=c3dcabd3cf74681c0a995719cb51e4c4&language=en-US'
    data = requests.get(url)
    data = data.json()
    print(data)
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


print(recommend('Batman Begins'))