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

# Show button 1
if st.button('Button 1'):
    st.write('Hello 1')

    # Show button 2
    if st.button('Button 2'):
        st.session_state.button2_clicked = True

# Show "Hello 2" message if button 2 is clicked
if st.session_state.get('button2_clicked', False):
    st.write('Hello 2')


