import streamlit as st
import requests
import wave
from tensorflow import keras
import numpy as np
import os
from tqdm import tqdm
from voice.splitter import split_video
from params import *
from prediction.preprocessor import preprocess_features
from prediction.registry import load_model

VOICE_SPLITS_DIRECTORY = os.path.join("voice","splits")
VOICE_RECORD_DIRECTORY = os.path.join("voice","records")
VOICE_RECORD_FILEPATH = os.path.join('voice','records','output.wav')
VOICE_DEMO1_FILEPATH = os.path.join("voice","pre_recorded","demo1","first_girl.wav")
VOICE_DEMO2_FILEPATH = os.path.join("voice","pre_recorded","demo2","Ruby_smooth.wav")

def goToChallenge(challenge_name):
    st.session_state.place = (
        challenge_name  # we are moving our character to other scene (e.g. sheepScene)
    )
    st.experimental_rerun()  # rerun is streamlit specific and rerund the app

def getPredictResult():
    # if PREDICT_RESOURCE == 'remote':
    #     # Send the voice data to backend
    #     url = 'http://localhost:8000/predict/'
    #     files = {'file': open('output.wav', 'rb')}
    #     response = requests.post(url, files=files)
    #     return np.array(response.json()) # expect to be an array of y value

    # elif PREDICT_RESOURCE == 'local':
    if not os.path.exists(VOICE_SPLITS_DIRECTORY):
        os.makedirs(VOICE_SPLITS_DIRECTORY)
        # Split the audio into clips
    split_video(VOICE_RECORD_FILEPATH)
        # Use model to predict
    model = load_model()
    assert model is not None
    X_processed = preprocess_features()
    y_pred = model.predict(X_processed)
    # st.write(f"predict:{y_pred}") # Keep for debugging purpose
    delete_files_in_directory(VOICE_SPLITS_DIRECTORY)
    return y_pred

def getPredictResultWithAllStutter():
    directory = os.path.join('voice','splits_test','isSoundRep')
    model = load_model()
    assert model is not None
    X_processed = preprocess_features(directory)
    y_pred = model.predict(X_processed)
    # st.write(f"predict:{y_pred}") # Keep for debugging purpose
    delete_files_in_directory(VOICE_SPLITS_DIRECTORY)
    return y_pred

def getPredictResultDemo1():
    split_video(VOICE_DEMO1_FILEPATH)

    model = load_model()
    assert model is not None
    X_processed = preprocess_features()
    y_pred = model.predict(X_processed)
    # st.write(f"predict:{y_pred}") # Keep for debugging purpose
    delete_files_in_directory(VOICE_SPLITS_DIRECTORY)
    return y_pred

def getPredictResultDemo2():
    split_video(VOICE_DEMO2_FILEPATH)
    model = load_model()
    assert model is not None
    X_processed = preprocess_features()
    y_pred = model.predict(X_processed)
    # st.write(f"predict:{y_pred}") # Keep for debugging purpose
    delete_files_in_directory(VOICE_SPLITS_DIRECTORY)
    return y_pred

def createAudioFile(wav_byte_data):
    if not os.path.exists(VOICE_RECORD_DIRECTORY):
        os.makedirs(VOICE_RECORD_DIRECTORY)
    sample_rate = 44100
    with wave.open(VOICE_RECORD_FILEPATH, "wb") as wf:
        wf.setnchannels(2)  # mono
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sample_rate)
        wf.writeframes(wav_byte_data)

def delete_files_in_directory(directory_path):
   try:
     files = os.listdir(directory_path)
     for file in files:
       file_path = os.path.join(directory_path, file)
       if os.path.isfile(file_path):
         os.remove(file_path)
     print(f"All files in {directory_path} deleted successfully.")
   except OSError:
     print("Error occurred while deleting files.")
