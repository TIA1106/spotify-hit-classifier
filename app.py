import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('hit_classifier_rf.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("Spotify Hit Song Predictor 🎵 (Random Forest Model)")

danceability = st.slider('Danceability', 0.0, 1.0, 0.5)
energy = st.slider('Energy', 0.0, 1.0, 0.5)
loudness = st.slider('Loudness', -60.0, 0.0, -20.0)
speechiness = st.slider('Speechiness', 0.0, 1.0, 0.1)
acousticness = st.slider('Acousticness', 0.0, 1.0, 0.5)
instrumentalness = st.slider('Instrumentalness', 0.0, 1.0, 0.0)
liveness = st.slider('Liveness', 0.0, 1.0, 0.2)
valence = st.slider('Valence', 0.0, 1.0, 0.5)
tempo = st.slider('Tempo', 50.0, 200.0, 120.0)

input_data = np.array([[danceability, energy, loudness, speechiness, acousticness,
                        instrumentalness, liveness, valence, tempo]])

input_scaled = scaler.transform(input_data)

if st.button('Predict'):
    result = model.predict(input_scaled)
    if result[0] == 1:
        st.success("🎉 This song has high chances of being a HIT!")
    else:
        st.info("😐 This song is unlikely to be a Hit.")
