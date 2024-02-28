# streamlit_audio_recorder by stefanrmmr (rs. analytics) - version January 2023

import streamlit as st
from st_audiorec import st_audiorec
import requests
import wave
import numpy as np
from scipy.io.wavfile import write

# DESIGN implement changes to the standard streamlit UI/UX
# --> optional, not relevant for the functionality of the component!
st.set_page_config(page_title="streamlit_audio_recorder")
# Design move app further up and remove top padding
st.markdown('''<style>.css-1egvi7u {margin-top: -3rem;}</style>''',
            unsafe_allow_html=True)
# Design change st.Audio to fixed height of 45 pixels
st.markdown('''<style>.stAudio {height: 45px;}</style>''',
            unsafe_allow_html=True)
# Design change hyperlink href link color
st.markdown('''<style>.css-v37k9u a {color: #ff4c4b;}</style>''',
            unsafe_allow_html=True)  # darkmode
st.markdown('''<style>.css-nlntq9 a {color: #ff4c4b;}</style>''',
            unsafe_allow_html=True)  # lightmode


def audiorec_demo_app():

    # TITLE and Creator information
    st.title('streamlit audio recorder')
    st.markdown('Implemented by '
        '[Stefan Rummer](https://www.linkedin.com/in/stefanrmmr/) - '
        'view project source code on '

        '[GitHub](https://github.com/stefanrmmr/streamlit-audio-recorder)')
    st.write('\n\n')

    # TUTORIAL: How to use STREAMLIT AUDIO RECORDER?
    # by calling this function an instance of the audio recorder is created
    # once a recording is completed, audio data will be saved to wav_audio_data

    wav_audio_data = st_audiorec() # tadaaaa! yes, that's it! :D

    # add some spacing and informative messages
    col_info, col_space = st.columns([0.57, 0.43])
    with col_info:
        st.write('\n')  # add vertical spacer
        st.write('\n')  # add vertical spacer
        st.write('The .wav audio data, as received in the backend Python code,'
                 ' will be displayed below this message as soon as it has'
                 ' been processed. [This informative message is not part of'
                 ' the audio recorder and can be removed easily] 🎈')

    if wav_audio_data is not None:
        # display audio data as received on the Python side
        col_playback, col_space = st.columns([0.58,0.42])
        with col_playback:
            st.audio(wav_audio_data, format='audio/wav')

        # samplerate = 44100; fs = 100
        # t = np.linspace(0., 1., samplerate)
        # amplitude = np.iinfo(np.int16).max
        # data = amplitude * np.sin(2. * np.pi * fs * t)
        # write("example.wav", samplerate, wav_audio_data.astype(np.int16))
        file_name = "output.wav"
        sample_rate = 44100
        with wave.open(file_name, "wb") as wf:
            wf.setnchannels(2)  # mono
            wf.setsampwidth(2)  # 16-bit
            wf.setframerate(sample_rate)
            wf.writeframes(wav_audio_data)

        # Show Send Audio Button
        if st.button('Send'):
            st.write('Sent')
            url = 'http://localhost:8000/predict/'
            files = {'file': open('output.wav', 'rb')}
            response = requests.post(url, files=files)

            print(response.json())


if __name__ == '__main__':
    # call main function
    audiorec_demo_app()
