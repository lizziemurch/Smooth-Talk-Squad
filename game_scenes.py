import streamlit as st
from streamlit_extras.stoggle import stoggle
import game_config
import game_def
import time
import random
from st_audiorec import st_audiorec
import game_util
from params import *

###############################################
#
#               intro Scene
#
################################################


def introScene():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Bangers&display=swap');

        /* Apply the Bangers font to the entire app */
        body {
            font-family: 'Bangers', cursive !important;
        }
        /* Custom styling for your element */
        .st-emotion-cache-1y4p8pa {
            padding-top: 1rem !important; /* Adjust the top padding */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source["introScene"])
    with col2:
        # scene text
        st.markdown(
            f'''<div class="fantasy-container">
            <p>🌟 Welcome to the Smooth Talk Squad! 🌟 You've arrived just in time! The Central Park Zoo is in a bit of a pickle — a group of cheeky animals has decided to go on an unexpected city tour, without telling anyone! 😲
            <br><br>
            🔍 Your Mission is to use your eagle-eyed super vision and your crystal-clear super voice to spot these adventurous animals. We'll share some sneaky photos from various corners of the city so you can help us look. 📸''',
            unsafe_allow_html=True,
        )

    bottom_text = st.columns(1)[0]  # Access the first item in the list returned by st.columns
    with bottom_text:
        st.markdown(
            f'''<div class="fantasy-container">
            <p>Before we begin, lets practice using the controls below. Press the <strong>START</strong> button and say
            “Smooth Talk Squad will save the day!” Then press the <strong>STOP</strong> button to stop. Once you have your
            recording, press <strong>SUBMIT</strong> to send the message to headquarters for analysis. 😎''',
            unsafe_allow_html=True,
        )

    wav_audio_data = st_audiorec() # tadaaaa! yes, that's it! :D

    if wav_audio_data is not None:
        # display audio data as received on the Python side
        col_playback, col_space = st.columns([0.58,0.42])
        with col_playback:
            st.audio(wav_audio_data, format='audio/wav')
        game_util.createAudioFile(wav_audio_data)

        # Show Send Audio Button
        if st.button('Send'):
            game_util.delete_files_in_directory(os.path.join("voice","splits"))
            y_pred = game_util.getPredictResult()
            if any(y > 0.4 for y in y_pred):
                st.write('Let\'s try again !')
            else:
                st.write('Good JOB !')
                st.balloons()

    if st.button('Next Challenge'):
        game_util.goToChallenge("peacockScene")



###############################################
#
# Peacock Scene (Scene #2)
#
################################################

def peacockScene():
    game_util.delete_files_in_directory(os.path.join("voice","splits"))
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Bangers&display=swap');

        /* Apply the Bangers font to the entire app */
        body {
            font-family: 'Bangers', cursive !important;
        }
        /* Custom styling for your element */
        .st-emotion-cache-1y4p8pa {
            padding-top: 1rem !important; /* Adjust the top padding */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # scene image
        st.image(game_config.image_source["peacockScene"])
    with col2:
        st.markdown(
            f'''<div class="fantasy-container" style="min-height:344px" </div>
            <p>Do you see any of the missing zoo animals in this picture?
            <br><br>
            👀 When you spot one of our furry (or feathery) escapees, hit the <strong>START</strong>
            button to record your message with the coolest, smoothest voice you can muster 😎.''',
            unsafe_allow_html=True,
        )
    bottom_text = st.columns(1)[0]  # Access the first item in the list returned by st.columns
    with bottom_text:
        st.markdown(
        f'''<div class="fantasy-container">
        <p>🗣️ Pro Tip: The smoother you speak, the quicker we can reunite these adventurous animals with their home.
        So, let's make it smooth and bring them back before they start taking selfies in Times Square! 🤳''',
        unsafe_allow_html=True,
        )

    wav_audio_data = st_audiorec() # tadaaaa! yes, that's it! :D

    if wav_audio_data is not None:
        # display audio data as received on the Python side
        col_playback, col_space = st.columns([0.58,0.42])
        with col_playback:
            st.audio(wav_audio_data, format='audio/wav')
        game_util.createAudioFile(wav_audio_data)

        # Show Send Audio Button
        if st.button('Send'):
            game_util.delete_files_in_directory(os.path.join("voice","splits"))
            y_pred = game_util.getPredictResult()
            if any(y > 0.7 for y in y_pred):
                st.write('Let\'s try again !')
            else:
                st.write('Good JOB !')
                st.balloons()



    # Pre-recorded voice for demo1
    audio_file = open("voice/pre_recorded/demo1/first_girl.wav", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mpeg")

    if st.button('Predict with Demo1 Clip'):
        y_pred = game_util.getPredictResultDemo1()
        if any(y > 0.8 for y in y_pred):
            st.header('Let\'s try again 🤔!')
        else:
            st.header('Good JOB 🏆!')
            st.balloons()

    # Pre-recorded voice for demo2
    audio_file = open("voice/pre_recorded/demo2/Lizzie_peacock_smooth.wav", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mpeg")

    if st.button('Predict with Demo2 Clip'):
        y_pred = game_util.getPredictResultDemo2()
        if any(y > 0.8 for y in y_pred):
            st.header('Let\'s try again 🤔!')
        else:
            st.header('Good JOB 🏆!')
            st.balloons()



    if st.button('Next Challenge'):
        game_util.goToChallenge("penguinScene")

###############################################
#
# Penguin Scene (Scene #3)
#
################################################

def penguinScene():
    game_util.delete_files_in_directory(os.path.join("voice","splits"))
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Bangers&display=swap');

        /* Apply the Bangers font to the entire app */
        body {
            font-family: 'Bangers', cursive !important;
        }
        /* Custom styling for your element */
        .st-emotion-cache-1y4p8pa {
            padding-top: 1rem !important; /* Adjust the top padding */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # scene image
        st.image(game_config.image_source["penguinScene"])
    with col2:
        st.markdown(
            f'''<div class="fantasy-container" style="min-height:344px" </div>
            <p>Do you see any of the missing zoo animals in this picture?
            <br><br>
            👀 When you spot one of our furry (or feathery) escapees, hit the <strong>START</strong>
            button to record your message with the coolest, smoothest voice you can muster 😎.''',
            unsafe_allow_html=True,
        )
    bottom_text = st.columns(1)[0]  # Access the first item in the list returned by st.columns
    with bottom_text:
        st.markdown(
        f'''<div class="fantasy-container">
        <p>🗣️ Pro Tip: The smoother you speak, the quicker we can reunite these adventurous animals with their home.
        So, let's make it smooth and bring them back before they start taking selfies in Times Square! 🤳''',
        unsafe_allow_html=True,
        )

    wav_audio_data = st_audiorec()

    if wav_audio_data is not None:
        # display audio data as received on the Python side
        col_playback, col_space = st.columns([0.58,0.42])
        with col_playback:
            st.audio(wav_audio_data, format='audio/wav')
        game_util.createAudioFile(wav_audio_data)

        # Show Send Audio Button
        if st.button('Send'):
            y_pred = game_util.getPredictResult()
            if any(y > 0.6 for y in y_pred):
                st.write('Let\'s try again !')
            else:
                st.write('Good JOB !')
                st.balloons()

    if st.button('Next Challenge'):
        game_util.goToChallenge("pandaScene")


###############################################
#
# Panda Scene (Scene #4)
#
################################################

def pandaScene():
    game_util.delete_files_in_directory(os.path.join("voice","splits"))
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Bangers&display=swap');

        /* Apply the Bangers font to the entire app */
        body {
            font-family: 'Bangers', cursive !important;
        }
        /* Custom styling for your element */
        .st-emotion-cache-1y4p8pa {
            padding-top: 1rem !important; /* Adjust the top padding */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # scene image
        st.image(game_config.image_source["pandaScene"])
    with col2:
        st.markdown(
            f'''<div class="fantasy-container" style="min-height:344px" </div>
            <p>Do you see any of the missing zoo animals in this picture?
            <br><br>
            👀 When you spot one of our furry (or feathery) escapees, hit the <strong>START</strong>
            button to record your message with the coolest, smoothest voice you can muster 😎.''',
            unsafe_allow_html=True,
        )
    bottom_text = st.columns(1)[0]  # Access the first item in the list returned by st.columns
    with bottom_text:
        st.markdown(
        f'''<div class="fantasy-container">
        <p>🗣️ Pro Tip: The smoother you speak, the quicker we can reunite these adventurous animals with their home.
        So, let's make it smooth and bring them back before they start taking selfies in Times Square! 🤳''',
        unsafe_allow_html=True,
        )

    wav_audio_data = st_audiorec()

    if wav_audio_data is not None:
        # display audio data as received on the Python side
        col_playback, col_space = st.columns([0.58,0.42])
        with col_playback:
            st.audio(wav_audio_data, format='audio/wav')
        game_util.createAudioFile(wav_audio_data)

        # Show Send Audio Button
        if st.button('Send'):
            y_pred = game_util.getPredictResult()
            if any(y > 0.6 for y in y_pred):
                st.write('Let\'s try again !')
            else:
                st.write('Good JOB !')
                st.balloons()

    if st.button('Next Challenge'):
        game_util.goToChallenge("foxScene")

###############################################
#
# Fox Scene (Scene #5)
#
################################################

def foxScene():
    game_util.delete_files_in_directory(os.path.join("voice","splits"))
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Bangers&display=swap');

        /* Apply the Bangers font to the entire app */
        body {
            font-family: 'Bangers', cursive !important;
        }
        /* Custom styling for your element */
        .st-emotion-cache-1y4p8pa {
            padding-top: 1rem !important; /* Adjust the top padding */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # scene image
        st.image(game_config.image_source["foxScene"])
    with col2:
        st.markdown(
            f'''<div class="fantasy-container" style="min-height:344px" </div>
            <p>Do you see any of the missing zoo animals in this picture?
            <br><br>
            👀 When you spot one of our furry (or feathery) escapees, hit the <strong>START</strong>
            button to record your message with the coolest, smoothest voice you can muster 😎.''',
            unsafe_allow_html=True,
        )
    bottom_text = st.columns(1)[0]  # Access the first item in the list returned by st.columns
    with bottom_text:
        st.markdown(
        f'''<div class="fantasy-container">
        <p>🗣️ Pro Tip: The smoother you speak, the quicker we can reunite these adventurous animals with their home.
        So, let's make it smooth and bring them back before they start taking selfies in Times Square! 🤳''',
        unsafe_allow_html=True,
        )

    wav_audio_data = st_audiorec()

    if wav_audio_data is not None:
        # display audio data as received on the Python side
        col_playback, col_space = st.columns([0.58,0.42])
        with col_playback:
            st.audio(wav_audio_data, format='audio/wav')
        game_util.createAudioFile(wav_audio_data)

        # Show Send Audio Button
        if st.button('Send'):
            y_pred = game_util.getPredictResult()
            if any(y > 0.6 for y in y_pred):
                st.write('Let\'s try again !')
            else:
                st.write('Good JOB !')
                st.balloons()

    if st.button('Next Challenge'):
        game_util.goToChallenge("monkeyScene")

###############################################
#
# Panda Scene (Scene #6)
#
################################################

def monkeyScene():
    game_util.delete_files_in_directory(os.path.join("voice","splits"))
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Bangers&display=swap');

        /* Apply the Bangers font to the entire app */
        body {
            font-family: 'Bangers', cursive !important;
        }
        /* Custom styling for your element */
        .st-emotion-cache-1y4p8pa {
            padding-top: 1rem !important; /* Adjust the top padding */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # scene image
        st.image(game_config.image_source["monkeyScene"])
    with col2:
        st.markdown(
            f'''<div class="fantasy-container" style="min-height:344px" </div>
            <p>Do you see any of the missing zoo animals in this picture?
            <br><br>
            👀 When you spot one of our furry (or feathery) escapees, hit the <strong>START</strong>
            button to record your message with the coolest, smoothest voice you can muster 😎.''',
            unsafe_allow_html=True,
        )
    bottom_text = st.columns(1)[0]  # Access the first item in the list returned by st.columns
    with bottom_text:
        st.markdown(
        f'''<div class="fantasy-container">
        <p>🗣️ Pro Tip: The smoother you speak, the quicker we can reunite these adventurous animals with their home.
        So, let's make it smooth and bring them back before they start taking selfies in Times Square! 🤳''',
        unsafe_allow_html=True,
        )

    wav_audio_data = st_audiorec()

    if wav_audio_data is not None:
        # display audio data as received on the Python side
        col_playback, col_space = st.columns([0.58,0.42])
        with col_playback:
            st.audio(wav_audio_data, format='audio/wav')
        game_util.createAudioFile(wav_audio_data)

        # Show Send Audio Button
        if st.button('Send'):
            y_pred = game_util.getPredictResult()
            if any(y > 0.6 for y in y_pred):
                st.write('Let\'s try again !')
            else:
                st.write('Good JOB !')
                st.balloons()

    if st.button('Next Challenge'):
        game_util.goToChallenge("tortoiseScene")

###############################################
#
# Tortoise Scene (Scene #7)
#
################################################

def tortoiseScene():

    game_util.delete_files_in_directory(os.path.join("voice","splits"))
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Bangers&display=swap');

        /* Apply the Bangers font to the entire app */
        body {
            font-family: 'Bangers', cursive !important;
        }
        /* Custom styling for your element */
        .st-emotion-cache-1y4p8pa {
            padding-top: 1rem !important; /* Adjust the top padding */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # scene image
        st.image(game_config.image_source["tortoiseScene"])
    with col2:
        st.markdown(
            f'''<div class="fantasy-container" style="min-height:344px" </div>
            <p>Do you see any of the missing zoo animals in this picture?
            <br><br>
            👀 When you spot one of our furry (or feathery) escapees, hit the <strong>START</strong>
            button to record your message with the coolest, smoothest voice you can muster 😎.''',
            unsafe_allow_html=True,
        )
    bottom_text = st.columns(1)[0]  # Access the first item in the list returned by st.columns
    with bottom_text:
        st.markdown(
        f'''<div class="fantasy-container">
        <p>🗣️ Pro Tip: The smoother you speak, the quicker we can reunite these adventurous animals with their home.
        So, let's make it smooth and bring them back before they start taking selfies in Times Square! 🤳''',
        unsafe_allow_html=True,
        )

    wav_audio_data = st_audiorec()

    if wav_audio_data is not None:
        # display audio data as received on the Python side
        col_playback, col_space = st.columns([0.58,0.42])
        with col_playback:
            st.audio(wav_audio_data, format='audio/wav')
        game_util.createAudioFile(wav_audio_data)

        # Show Send Audio Button
        if st.button('Send'):
            y_pred = game_util.getPredictResult()
            if any(y > 0.6 for y in y_pred):
                st.write('Let\'s try again !')
            else:
                st.write('Good JOB !')
                st.balloons()

    if st.button('Next Challenge'):
        game_util.goToChallenge("finalScene")

###############################################
#
# Final Scene (Scene #8)
#
################################################

def finalScene():
    game_util.delete_files_in_directory(os.path.join("voice","splits"))
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Bangers&display=swap');

        /* Apply the Bangers font to the entire app */
        body {
            font-family: 'Bangers', cursive !important;
        }
        /* Custom styling for your element */
        .st-emotion-cache-1y4p8pa {
            padding-top: 1rem !important; /* Adjust the top padding */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    col1, col2 = st.columns(2, gap="small")
    with col1:
        # scene image
        st.image(game_config.image_source["finalScene"])
    with col2:
        st.markdown(
            f'''<div class="fantasy-container" style="min-height:344px" </div>
            <p>🎉 Mission Accomplished! 🎉
            <br><br>
            Congratulations, Super Sleuths of the Smooth Talk Squad! 🌟 You've done it!
            Thanks to your eagle eyes and silky smooth talking, all our adventurous animal
            friends are ready to head back to their cozy homes at the Central Park Zoo. 🐾🏠
            <br><br>
            Your dedication, bravery, and superb detective skills have saved the day, turning
            a potential animal escapade into an unforgettable adventure.''',
            unsafe_allow_html=True,
        )
    bottom_text = st.columns(1)[0]  # Access the first item in the list returned by st.columns
    with bottom_text:
        st.markdown(
        f'''<div class="fantasy-container">
        <p> 🗣️ Before we bid farewell, we have one last mission for you. Hit the START button
        one more time to record a message, but this time,share your wisest piece of advice for
        our furry and feathered friends as they return to the zoo. Until our next adventure,
        keep your eyes peeled, your voice smooth, and your heart open to the wonders around you.
        <br><br>
        🌍✨ The Smooth Talk Squad will return... and we hope you will too!''',
        unsafe_allow_html=True,
        )

    wav_audio_data = st_audiorec()

    if wav_audio_data is not None:
        # display audio data as received on the Python side
        col_playback, col_space = st.columns([0.58,0.42])
        with col_playback:
            st.audio(wav_audio_data, format='audio/wav')
        game_util.createAudioFile(wav_audio_data)

        # Show Send Audio Button
        if st.button('Send'):
            y_pred = game_util.getPredictResult()
            if any(y > 0.6 for y in y_pred):
                st.write('Let\'s try again !')
            else:
                st.write('Good JOB !')
                st.balloons()
