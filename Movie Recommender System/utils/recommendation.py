import pandas as pd ## this library is used for data processing, csv files read I/O
import numpy as np ## this is used for linear algebra
movies=pd.read_csv('data/tmdb_5000_movies.csv')
credits=pd.read_csv('data/tmdb_5000_credits.csv')

#merge two dataset and assign to movies dataset

movies=movies.merge(credits, on='title')

# only select useful features for model creation
movies=movies[['movie_id','title','overview','genres','keywords','cast','crew']]


