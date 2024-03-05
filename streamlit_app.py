import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.stoggle import stoggle
from streamlit_extras.metric_cards import style_metric_cards
import time
import random
import game_scenes

# additional components from https://extras.streamlit.app/

# -------------- app config ---------------

st.set_page_config(page_title="Smooth Talk Squad", page_icon="🦸🏻‍♀️")

# define external css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


###############################################
#
#
#           VARIABLES DEFINITION
#
#
################################################

# variable responsible for checking if player provided his name and game can be started
start = False

# set session states
# this is streamlit specific. For more contex please check streamlit documenation

# if "health" not in st.session_state:
#     st.session_state["health"] = 100
# if "mana" not in st.session_state:
#     st.session_state["mana"] = 80
# if "gold" not in st.session_state:
#     st.session_state["gold"] = 5
if "place" not in st.session_state:
    st.session_state["place"] = "introScene"
# if "sheep_anger" not in st.session_state:
#     st.session_state["sheep_anger"] = 0
# if "sword" not in st.session_state:
#     st.session_state["sword"] = 0
# if "dragon_alive" not in st.session_state:
#     st.session_state["dragon_alive"] = 1
# if "dragon_hp" not in st.session_state:
#     st.session_state["dragon_hp"] = 20
# if "temp" not in st.session_state:
#     st.session_state["temp"] = ""
if "counter" not in st.session_state:
    st.session_state["counter"] = 0
if "scenes_counter" not in st.session_state:
    st.session_state["scenes_counter"] = {
        "intro_counter": 0,
        "cave_counter": 0,
        "trip_counter": 0,
        "elf_counter": 0,
    }


###############################################
#
#
#               GAME ENGINE
#
#
################################################

# ---------------- CSS ----------------

local_css("style.css")

# ----------------- game start --------


welcome = st.empty()
welcome.title("Smooth  Talk  Squad")

if st.session_state.place == "introScene":
    game_scenes.introScene()
elif st.session_state.place == "peacockScene":
    game_scenes.peacockScene()
elif st.session_state.place == "penguinScene":
    game_scenes.penguinScene()
elif st.session_state.place == "pandaScene":
    game_scenes.pandaScene()
elif st.session_state.place == "foxScene":
    game_scenes.foxScene()
elif st.session_state.place == "monkeyScene":
    game_scenes.monkeyScene()
elif st.session_state.place == "tortoiseScene":
    game_scenes.tortoiseScene()
elif st.session_state.place == "finalScene":
    game_scenes.finalScene()

components.html(
    f"""
        <div>some hidden container</div>
        <p>{st.session_state.counter}</p>
        <script>
            var input = window.parent.document.querySelectorAll("input[type=text]");
            for (var i = 0; i < input.length; ++i) {{
                input[i].focus();
            }}
    </script>
    """,
    height=0,
)

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
