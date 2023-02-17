import streamlit as st
import pandas as pd
import numpy as np
from google.oauth2 import service_account
import random

CARD_WIDTH = 100


def display_cards(cards):

    st.subheader('Use all these cards:')
    col1, col2, col3, col4, col5 = st.columns(5)
    # Add a card to each column
    with col1:
        st.image(f"cards/{cards[0]}.jpg", width=CARD_WIDTH)
    with col2:
        st.image(f"cards/{cards[1]}.jpg", width=CARD_WIDTH)
    with col3:
        st.image(f"cards/{cards[2]}.jpg", width=CARD_WIDTH)
    with col4:
        st.image(f"cards/{cards[3]}.jpg", width=CARD_WIDTH)
    with col5:
        st.image(f"cards/{cards[4]}.jpg", width=CARD_WIDTH)

    st.write("")
    st.write("")
    st.subheader('to reach:')
    # Add a card to each column
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        st.image(f"cards/{cards[5]}.jpg", width=CARD_WIDTH)

def pick_cards():
    # Create a list of cards with the specified probabilities
    cards = [i for i in range(1, 11) for _ in range(3)]
    cards += [i for i in range(11, 18) for _ in range(2)]
    cards += [i for i in range(18, 25)]

    # Shuffle the deck
    random.shuffle(cards)

    # Pick 6 cards from the deck
    return random.sample(cards, 6)


# deal_cards = st.button('New Cards')

# if deal_cards:
#     cards = pick_cards()
#     display_cards(cards)

if "button1" not in st.session_state:
    st.session_state["button1"] = False

if "button2" not in st.session_state:
    st.session_state["button2"] = False


if st.button("Button1"):
    st.session_state["button1"] = not st.session_state["button1"]

if st.session_state["button1"]:
    if st.button("Button2"):
        st.session_state["button2"] = not st.session_state["button2"]

if st.session_state["button2"]:
    st.write("**Button2!!!**")


# Print the session state to make it easier to see what's happening
st.write(
    f"""
    ## Session state:
    {st.session_state["button1"]=}

    {st.session_state["button2"]=}

    """
)


