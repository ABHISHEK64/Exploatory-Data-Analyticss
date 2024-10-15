import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movies_index=movies[movies['Title_x']==movie].index[0]
    movies_list=sorted(list(enumerate(similarity[movies_index])),reverse=True,key= lambda x:x[1])[1:8]
    recommend_mve=[]
    recommend_images=[]
    for i in movies_list:
        recommend_mve.append(movies.iloc[i[0]].Title_x)
        recommend_images.append(movies.iloc[i[0]].image)
    return recommend_mve,recommend_images

movie_path=r'C:\Users\abhis\Documents\imdb_data\imdb_data\movies.pkl'
model_path=r'C:\Users\abhis\Documents\imdb_data\imdb_data\similarity.pkl'
movies=pickle.load(open(movie_path,'rb'))
similarity=pickle.load(open(model_path,'rb'))
movies_list=movies['Title_x'].values
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
