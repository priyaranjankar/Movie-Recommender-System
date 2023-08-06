import streamlit as st
import pickle
import requests

#note: Replace API key with your own key from the tmdb website instead of the one mentioned here
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=4438749923cfa9c6f7ea4aaf350f4gh6".format(movie_id)
    response = requests.get(url)
    movie_details = response.json()
    poster_path = movie_details['poster_path']
    full_path = "https://image.tmdb.org/t/p/original/" + poster_path
    return full_path
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        # get movie title into recommended movies
        recommended_movie_names.append(movies.iloc[i[0]].title)
        # fetch movie poster using movie id from API
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie_names,recommended_movie_posters

movies = pickle.load(open('movies_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
st.header('Movie Recommender System')

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list)

if st.button('Recommend movies'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
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
