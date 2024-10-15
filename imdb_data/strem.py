import streamlit as st
import pickle
import pandas as pd
import zipfile
import os
import io
import requests

def recommend(movie):
    movies_index=movie_path[movie_path['Title_x']==movie].index[0]
    movies_list=sorted(list(enumerate(model_path[movies_index])),reverse=True,key= lambda x:x[1])[1:8]
    recommend_mve=[]
    recommend_images=[]
    for i in movies_list:
        recommend_mve.append(movie_path.iloc[i[0]].Title_x)
        recommend_images.append(movie_path.iloc[i[0]].image)
    return recommend_mve,recommend_images
zip_path = r'https://raw.githubusercontent.com/ABHISHEK64/Exploatory-Data-Analyticss/main/imdb_data/movies.zip'

response = requests.get(zip_path)
if response.status_code == 200:
    # Open the ZIP file from the downloaded content in memory
    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
        # Extract the Tweets.pkl file in memory
        with zip_ref.open('movies.pkl') as pkl_file:
            movie_path = pickle.load(pkl_file)
        with zip_ref.open('similarity.pkl')as pkl_file:
            model_path=pickle.load(pkl_file)

else:
    st.error("Failed to download the ZIP file from GitHub.")

movies_list=movie_path['Title_x'].values
st.title("Movies Recomender System")

selected_movies=st.selectbox('Select your favourte movies',(movies_list))

if st.button('Recommend'):
    recommdations,images=recommend(selected_movies)
    cols=st.columns(3)
    for i in range(len(recommdations)):
        col=cols[i%3]
        with col:
                
        
                st.image(images[i])
                st.write(recommdations[i])
