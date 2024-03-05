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
    .st-emotion-cache-1y4p8pa {
        padding-top: 3rem !important; /* Adjust the top padding to 1rem */
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
        if st.session_state["scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f'''<div class="fantasy-container">
                <p>🌟 Welcome to the Smooth Talk Squad! 🌟 You've arrived just in time! The Central Park Zoo is in a bit of a pickle — a group of cheeky animals has decided to go on an unexpected city tour, without telling anyone! 😲
                <br><br>
                🔍 Your Mission is to use your eagle-eyed super vision and your crystal-clear super voice to spot these adventurous animals. We'll share some sneaky photos from various corners of the city so you can help us look. 📸''',
                unsafe_allow_html=True,
            )

        else:
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
            y_pred = game_util.getPredictResult()
            if any(y > 0.6 for y in y_pred):
                st.write('Let\'s try again !')
            else:
                st.write('Good JOB !')
                st.balloons()

    if st.button('Next Challenge'):
        game_util.goToChallenge("peacockScene")

    if st.button('Predict with Stuttering Clips'):
        y_pred = game_util.getPredictResultWithAllStutter()
        if any(y > 0.6 for y in y_pred):
            st.write('Let\'s try again !')
        else:
            st.write('Good JOB !')
            st.balloons()
###############################################
#
# Peacock Scene (Scene #2, Formerly Sheep Scene)
#
################################################


def peacockScene():

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
            y_pred = game_util.getPredictResult()
            if any(y > 0.6 for y in y_pred):
                st.write('Let\'s try again !')
            else:
                st.write('Good JOB !')
                st.balloons()

    if st.button('Next Challenge'):
        game_util.goToChallenge("PenguinScene")

###############################################
#
# Penguin Scene (Scene #3, Formerly Cave Scene)
#
################################################


# def penguinScene():

#     # possible actions
#     directions = ["up", "back", "help"]

#     col1, col2 = st.columns(2, gap="small")
#     with col1:
#         # main_image
#         st.image(game_config.image_source["penguinScene"])
#         st.write("Dark cave")
#     with col2:
#         # scene text
#         # conditional if you have already seen the scene
#         if st.session_state["scenes_counter"]["cave_counter"] == 0:
#             st.markdown(
#                 f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>After walking for 2 hours through the enchanted forest, you stumble across a mysterious cave. Legends say that if you stare into the abyss, the abyss will stare back at you. A faint glimmer of light seems to be emanating from the depths of the cave. An eerie chill runs down your spine as you walk closer, but you can\'t help but be curious of the unknown. Are you brave enough to enter the depths of this mysterious cave, despite the fear of the unknown darkness?</p></div>',
#                 unsafe_allow_html=True,
#             )
#             audio_file = open("streamlit/audio/cave.mp3", "rb")
#             audio_bytes = audio_file.read()
#             st.audio(audio_bytes, format="audio/mpeg")
#         else:
#             st.markdown(
#                 f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>You are back at the cave.</p></div>',
#                 unsafe_allow_html=True,
#             )

#     directions_container = st.empty()

#     # caption below input
#     st.caption(game_config.caption_below_input)

#     if st.session_state["scenes_counter"]["trip_counter"] == 0:
#         st.success("You feel exhausted and lose -5HP")
#         st.session_state.health = st.session_state.health - 5
#         st.session_state["scenes_counter"]["trip_counter"] = 1

#     directions_container.text_input(
#         "What to do?",
#         key="caveSceneActions",
#         on_change=game_def.clear,
#         args=["caveSceneActions"],
#     )

#     scene_action = st.session_state["temp"]

#     if scene_action.lower() in directions:
#         # --- HELP ---
#         # ------------
#         if scene_action.lower() == "help":
#             st.info(f'Potential actions: {", ".join(directions)}')
#         # --- back ---
#         # ------------
#         if scene_action.lower() == "back":
#             st.session_state["scenes_counter"]["cave_counter"] += 1
#             st.session_state.place = "introScene"
#             game_def.temp_clear()
#             st.experimental_rerun()
#         # --- up ---
#         # ------------
#         if scene_action.lower() == "up":
#             st.session_state["scenes_counter"]["cave_counter"] += 1
#             st.session_state.place = "poScene"
#             game_def.temp_clear()
#             st.experimental_rerun()

#     else:
#         # what should happen if wrong action is selected
#         if scene_action != "":
#             st.info("Please provide right input")
#             dir = f'Potential actions: {", ".join(directions)}'
#             stoggle("Help", dir)
#             st.write("")
