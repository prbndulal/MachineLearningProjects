import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
from utils import save_model,movies_new_df,recommend

import joblib

    #save_model( movies_new_df,"movielist.model")


 


if __name__ == '__main__':
    st.title("Movie Recommender System") 
    movie_list = joblib.load('models/movielist.model')
    movie_list=movie_list['title'].values
    selected_movie_name =st.selectbox('Please select movie',movie_list)
    if st.button('Recommend'):
        names,posters=recommend(selected_movie_name)
        for i in recommendations:
            


            
            st.write(i)


    print(movie_list)
    #show_recommended_movies()
