import pandas as pd ## this library is used for data processing, csv files read I/O
import numpy as np ## this is used for linear algebra
from helper import convert,convert3text,fetch_director,stem
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies=pd.read_csv('../data/tmdb_5000_movies.csv')
credits=pd.read_csv('../data/tmdb_5000_credits.csv')

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

def recommend(movie):
    movie_index=movies_new_df[movies_new_df['title']==movie].index[0]
    distances=similarity[movie_index]
    pass



print(similarity[0])