import pickle 
import streamlit as st
import requests 

import pandas as pd 
# print("pandas version")
# print(pd.__version__)


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=a2ced4cef845724840b928f1233ec3ff".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path



def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])) , reverse=True , key = lambda x:x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name , recommended_movies_poster



st.header("Movie Recommendation System")
movies = pd.read_pickle(open('artificats/movie_list.pkl', 'rb'))
similarity = pd.read_pickle(open('artificats/similarity.pkl' , 'rb'))

movie_list = movies['title'].values

selected_movie = st.selectbox('Type or select a movie for recommendation' , movie_list)


# Your existing code for the recommendation display
if st.button('Show recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(recommended_movies_poster[0], caption=recommended_movies_name[0], width=None)
        st.markdown(
            """
            <style>
                div[data-testid="stImage"] {
                    margin-bottom: 20px;
                    text-align: center;
                    border-radius: 10px;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.image(recommended_movies_poster[1], caption=recommended_movies_name[1], width=None)

    with col3:
        st.image(recommended_movies_poster[2], caption=recommended_movies_name[2], width=None)

    with col4:
        st.image(recommended_movies_poster[3], caption=recommended_movies_name[3], width=None)

    with col5:
        st.image(recommended_movies_poster[4], caption=recommended_movies_name[4], width=None)
