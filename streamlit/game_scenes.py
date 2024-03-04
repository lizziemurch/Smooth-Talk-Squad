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
            print(y_pred)
            if any(y > float(Y_THRESHOLD) for y in y_pred):
                st.write('Let\'s try again !')
            else:
                st.write('Good JOB !')
                st.balloons()

    if st.button('Next Challenge'):
        game_util.goToChallenge("peacockScene")


###############################################
#
# Peacock Scene (Scene #2, Formerly Sheep Scene)
#
################################################


def peacockScene():

    # # possible actions
    # directions = ["left", "right", "back", "pet", "help"]

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

    # audio_file = open("streamlit/audio/sheep.mp3", "rb")
    # audio_bytes = audio_file.read()
    # st.audio(audio_bytes, format="audio/mpeg")

    wav_audio_data = st_audiorec() # tadaaaa! yes, that's it! :D

    if wav_audio_data is not None:
        # display audio data as received on the Python side
        col_playback, col_space = st.columns([0.58,0.42])
        with col_playback:
            st.audio(wav_audio_data, format='audio/wav')
        game_util.createAudioFile(wav_audio_data)

        # Show Send Audio Button
        if st.button('Send'):
            game_util.getPredictResult()

    if st.button('Next Challenge'):
        game_util.goToChallenge("PenguinScene")



###############################################
#
# Penguin Scene (Scene #3, Formerly Cave Scene)
#
################################################


def penguinScene():

    # possible actions
    directions = ["up", "back", "help"]

    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source["penguinScene"])
        st.write("Dark cave")
    with col2:
        # scene text
        # conditional if you have already seen the scene
        if st.session_state["scenes_counter"]["cave_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>After walking for 2 hours through the enchanted forest, you stumble across a mysterious cave. Legends say that if you stare into the abyss, the abyss will stare back at you. A faint glimmer of light seems to be emanating from the depths of the cave. An eerie chill runs down your spine as you walk closer, but you can\'t help but be curious of the unknown. Are you brave enough to enter the depths of this mysterious cave, despite the fear of the unknown darkness?</p></div>',
                unsafe_allow_html=True,
            )
            audio_file = open("streamlit/audio/cave.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")
        else:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>You are back at the cave.</p></div>',
                unsafe_allow_html=True,
            )

    directions_container = st.empty()

    # caption below input
    st.caption(game_config.caption_below_input)

    if st.session_state["scenes_counter"]["trip_counter"] == 0:
        st.success("You feel exhausted and lose -5HP")
        st.session_state.health = st.session_state.health - 5
        st.session_state["scenes_counter"]["trip_counter"] = 1

    directions_container.text_input(
        "What to do?",
        key="caveSceneActions",
        on_change=game_def.clear,
        args=["caveSceneActions"],
    )

    scene_action = st.session_state["temp"]

    if scene_action.lower() in directions:
        # --- HELP ---
        # ------------
        if scene_action.lower() == "help":
            st.info(f'Potential actions: {", ".join(directions)}')
        # --- back ---
        # ------------
        if scene_action.lower() == "back":
            st.session_state["scenes_counter"]["cave_counter"] += 1
            st.session_state.place = "introScene"
            game_def.temp_clear()
            st.experimental_rerun()
        # --- up ---
        # ------------
        if scene_action.lower() == "up":
            st.session_state["scenes_counter"]["cave_counter"] += 1
            st.session_state.place = "poScene"
            game_def.temp_clear()
            st.experimental_rerun()

    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("Please provide right input")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")


###############################################
#
#               po Scene
#
################################################


def poScene():

    # possible actions
    directions = ["left", "right", "back", "buy", "help"]

    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source["poScene"])
        st.write("Product manager's hideout")
    with col2:
        # scene text
        st.markdown(
            f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>In the dark, you see a young man. He was once a renowned product manager, who worked diligently to make the world a better place. But one day, he was attempting to add comments to Jira, when suddenly, something went wrong and his work didn\'t save. As a result, he was cursed to sell swords in a mystical land, far away from his home. He mutters that the price of 30 gold feels right, and then he offers a warning - if you go right, you will meet a dangerous dragon. He reminds you to keep left if you want to find the exit.</p></div>',
            unsafe_allow_html=True,
        )
        audio_file = open("streamlit/audio/po.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mpeg")

    directions_container = st.empty()

    # caption below input
    st.caption(game_config.caption_below_input)

    directions_container.text_input(
        "What to do?",
        key="poSceneActions",  # potentially dynamic key based on function name?
        on_change=game_def.clear,
        args=["poSceneActions"],  # potentially dynamic key based on function name?
    )

    scene_action = st.session_state["temp"]

    if scene_action.lower() in directions:
        # --- HELP ---
        # ------------
        if scene_action.lower() == "help":
            st.info(f'Potential actions: {", ".join(directions)}')
        # --- LEFT ---
        # ------------
        if scene_action.lower() == "left":
            st.session_state.place = "dragonScene"
            game_def.temp_clear()
            st.experimental_rerun()
        # --- RIGHT OR BACK ---
        # ------------
        if scene_action.lower() == "right" or scene_action.lower() == "back":
            st.session_state.place = "caveScene"
            game_def.temp_clear()
            st.experimental_rerun()
        # --- BUY ---
        # ------------
        if scene_action.lower() == "buy":
            my_bar = st.empty()
            my_bar.progress(0)

            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1)
            my_bar.empty()
            if st.session_state["gold"] >= 30:
                st.success("Acquired sword")
                st.session_state["gold"] = st.session_state["gold"] - 30
                st.session_state["sword"] = 1
            else:
                st.success("You don't have enough money")

    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("Please provide right input")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")


###############################################
#
#               dragon SCENE
#
################################################


def dragonScene():

    # possible actions
    directions = ["fight", "up", "back", "help"]

    # main_image

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(game_config.image_source["dragonScene"])
        st.write("Dragon's lair")

    with col2:
        # scene text
        st.markdown(
            f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Oh no! PM was wrong about going left! It\'s a Neural Network AI Deep Learning Big Data Generated Dragon! (NNADLBDGD)</p></div>',
            unsafe_allow_html=True,
        )
        audio_file = open("streamlit/audio/dragon.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mpeg")

    # without a sword you will die
    if st.session_state.sword == 0:
        st.success(
            "Dragon uses matrix multiplication and you get hit in the head by loose neuron. You don't have anything to defend yourself."
        )
        st.success(
            "Unfortunatelly this is where your adventure ends. But could you have done something differently?"
        )
        if st.button("Restart"):
            game_def.restart_session()
            st.session_state.place = "introScene"
            game_def.temp_clear()
            st.experimental_rerun()
    else:

        st.success(
            "Fortunatelly you have a sword so you can defend yourself from the dragon! Do you wanna fight it?"
        )
        directions_container = st.empty()
        st.caption(
            'Use mouse or [Tab] to focus on input field. To check potential actions, type "help".'
        )

        # # st.session_state
        # scene_action = directions_container.text_input(
        #     "What to do?", key="dragonSceneActions"
        # )

        directions_container.text_input(
            "What to do?",
            key="dragonSceneActions",  # potentially dynamic key based on function name?
            on_change=game_def.clear,
            args=[
                "dragonSceneActions"
            ],  # potentially dynamic key based on function name?
        )

        scene_action = st.session_state["temp"]

        if scene_action.lower() in directions:
            if scene_action.lower() == "help":
                st.info(f'Potential actions: {", ".join(directions)}')
            if scene_action.lower() == "fight":
                my_bar = st.empty()
                my_bar.progress(0)

                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1)
                my_bar.empty()
                if st.session_state.dragon_alive == 1:

                    st.success(
                        "Your matrix multiplication skills are better than dragons. Who would have guessed that these algebra classes would be useful after all?"
                    )
                    damage = random.randint(5, 10)
                    st.success("Dragon loses " + str(damage) + " HP")

                    st.session_state["dragon_hp"] = st.session_state[
                        "dragon_hp"
                    ] - random.randint(0, damage)

                    damage = random.randint(0, 8)
                    st.success(
                        "Dragon hits you back and you lose " + str(damage) + " HP"
                    )

                    st.session_state["health"] = st.session_state["health"] - damage
                    if st.session_state["dragon_hp"] <= 0:
                        st.session_state.dragon_alive = 0
                        st.success("DRAGON IS DEAD or at least to you")
                else:
                    st.success("DRAGON IS DEAD or at least to you")

            if scene_action.lower() == "up":
                if st.session_state.dragon_alive == 1:
                    st.success("Dragon is still alive. Fight or flight!")
                else:
                    st.session_state.place = "libraryScene"
                    game_def.temp_clear()
                    st.experimental_rerun()

            if scene_action.lower() == "back":
                st.session_state.place = "poScene"
                game_def.temp_clear()
                st.experimental_rerun()

        else:
            # what should happen if wrong action is selected
            if scene_action != "":
                st.info("Please provide right input")
                dir = f'Potential actions: {", ".join(directions)}'
                stoggle("Help", dir)
                st.write("")


###############################################
#
#               southpath Scene
#
################################################


def southpathScene():

    scene_identifier = "southpath"

    # possible actions
    directions = ["north", "south", "back", "help"]

    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source[scene_identifier + "Scene"])
        st.write("South path")
    with col2:

        scene_prompt = """As you embark on your journey, you find yourself walking south through the enchanted forest.
        The air is thick with magic, and the trees tower above you like guardians of the land.
        The forest floor is soft and cushioned with fallen leaves and moss, and the rustling of leaves and chirping of creatures fill the air.
        Every step you take feels like you're entering deeper into a world of mystery and wonder.
        The further you venture, the more you begin to sense that you are not alone.
        Shadows dart between trees, and the occasional eerie howl sends shivers down your spine.
        This enchanted forest is full of secrets waiting to be uncovered, and you are determined to find them all.
        """

        # scene text
        # conditional if you have already seen the scene

        st.markdown(
            f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>{scene_prompt}</p></div>',
            unsafe_allow_html=True,
        )
        audio_file = open("streamlit/audio/south.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mpeg")

    directions_container = st.empty()

    # caption below input
    st.caption(game_config.caption_below_input)

    directions_container.text_input(
        "What to do?",
        key=scene_identifier + "SceneActions",
        on_change=game_def.clear,
        args=[scene_identifier + "SceneActions"],
    )

    scene_action = st.session_state["temp"]

    if scene_action.lower() in directions:
        # --- HELP ---
        # ------------
        if scene_action.lower() == "help":
            st.info(f'Potential actions: {", ".join(directions)}')
        # --- back ---
        # ------------
        if scene_action.lower() == "back":
            st.session_state.place = "introScene"
            game_def.temp_clear()
            st.experimental_rerun()
        # --- up ---
        # ------------
        if scene_action.lower() == "north":
            st.session_state.place = "introScene"
            game_def.temp_clear()
            st.experimental_rerun()
        if scene_action.lower() == "south":
            st.session_state.place = "elfScene"
            game_def.temp_clear()
            st.experimental_rerun()
    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("Please provide right input")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")


###############################################
#
#               elf Scene
#
################################################


def elfScene():

    scene_identifier = "elf"

    # possible actions
    directions = ["north", "back", "help", "accept"]

    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image(game_config.image_source[scene_identifier + "Scene"])
        st.write("Elf sorceress")
    with col2:

        scene_prompt = """As you journey through the fantastical land, you come across a red-haired elf sorceress.
        She is poised and graceful, with piercing blue eyes that seem to look straight into your soul.
        Her movements are fluid and almost dance-like, as she casts spell after spell with ease.
        Her power is palpable, and it is clear that she is not someone to be trifled with.
        She speaks to you in a voice that is both musical and commanding, and you can tell that she is a being of great wisdom and knowledge.
        She tells you that she has been watching you, and that she senses that you are destined for great things.
        She offers to assist you on your journey, and you can feel that her magic could prove invaluable.
        """

        # scene text
        # conditional if you have already seen the scene
        if st.session_state["scenes_counter"]["elf_counter"] == 0:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>{scene_prompt}</p></div>',
                unsafe_allow_html=True,
            )
            audio_file = open("audio/elf1.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")
        else:
            st.markdown(
                f'<div class="fantasy-container"><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.gif" class="image"><p>Sorcerres says: "We should go back."</p></div>',
                unsafe_allow_html=True,
            )
            audio_file = open("streamlit/audio/elf2.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mpeg")

    directions_container = st.empty()

    # caption below input
    st.caption(game_config.caption_below_input)

    directions_container.text_input(
        "What to do?",
        key=scene_identifier + "SceneActions",
        on_change=game_def.clear,
        args=[scene_identifier + "SceneActions"],
    )

    scene_action = st.session_state["temp"]

    if scene_action.lower() in directions:
        # --- HELP ---
        # ------------
        if scene_action.lower() == "help":
            st.info(f'Potential actions: {", ".join(directions)}')
        # --- back ---
        # ------------
        if scene_action.lower() == "back":
            st.session_state.place = "southpathScene"
            game_def.temp_clear()
            st.experimental_rerun()
        # --- up ---
        # ------------
        if scene_action.lower() == "north":
            st.session_state.place = "southpathScene"
            game_def.temp_clear()
            st.experimental_rerun()
        if scene_action.lower() == "accept":
            st.info("Elf sorceress joined the party")
            st.session_state["scenes_counter"]["elf_counter"] += 1
    else:
        # what should happen if wrong action is selected
        if scene_action != "":
            st.info("Please provide right input")
            dir = f'Potential actions: {", ".join(directions)}'
            stoggle("Help", dir)
            st.write("")


###############################################
#
#               library SCENE
#
################################################


def libraryScene():

    # possible actions
    directions = ["left", "right"]

    # main_image
    st.image(game_config.image_source["libraryScene"])

    # scene text
    st.snow()
    st.title("Congratulations " + st.session_state.player_name + "!")

    st.markdown(
        f'<div class="fantasy-container"><p>You enter the dragon vault, but instead of gold, you find a Streamlit documentation library!<br><br>All the power is now in your hands. Would you make the documentation available for others? Or keep it only for yourself and make the sickest app in the world? The possibilities offered by Streamlit amaze you.<br><br>One man once said that with great power comes great responsibility (he was talking to a spider, but whatever).<br><br>Use your new power wisely.</div>',
        unsafe_allow_html=True,
    )
    st.success("Thank you for playing SteamlitLand Adventure RPG!")
    st.info("If you liked the game you can like ❤️ the community post and share it 🙂")
    st.info("Credits: Created by @TomJohn")
    st.info("Top players: knight @Courtland_Goldengate")
    st.caption("beta version")
