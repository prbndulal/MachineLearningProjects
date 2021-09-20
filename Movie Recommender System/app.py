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
        recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
        with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])

        with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
        with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
        with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])


    print(movie_list)
    #show_recommended_movies()
