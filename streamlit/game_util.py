import streamlit as st
import requests
import random
import wave

def goToChallenge(challenge_name):
    st.session_state.place = (
        challenge_name  # we are moving our character to other scene (e.g. sheepScene)
    )
    st.experimental_rerun()  # rerun is streamlit specific and rerund the app

def getPredictResult():
    # Send the voic data to backend
    url = 'http://localhost:8000/predict/'
    files = {'file': open('output.wav', 'rb')}
    response = requests.post(url, files=files)
    predict_result = response.json()

    # We need to change this part when we finalize the response in our API
    random_number = random.randint(1, 100)
    if len(predict_result["filename"]) > 0 and (random_number%2) == 0:
        st.write('Good JOB !')
        st.balloons()
    else:
        st.write('Let\'s try again !')

def createAudioFile(wav_byte_data):
    file_name = "output.wav"
    sample_rate = 44100
    with wave.open(file_name, "wb") as wf:
        wf.setnchannels(2)  # mono
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sample_rate)
        wf.writeframes(wav_byte_data)
