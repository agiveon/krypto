import streamlit as st
import pandas as pd
import numpy as np
from google.oauth2 import service_account
import random
import itertools
import pickle

st.set_page_config(page_title="Krypto - The Math Game")

st.write('''<style>

[data-testid="column"] {
    width: calc(20% - 1rem) !important;
    flex: 1 1 calc(20% - 1rem) !important;
    min-width: calc(20% - 1rem) !important;
}
</style>''', unsafe_allow_html=True)

hide_img_fs = ''' <style> button[title="View fullscreen"]{ visibility: hidden;} </style> ''' 
st.markdown(hide_img_fs, unsafe_allow_html=True)

def display_cards(cards):

    st.subheader('Use all these cards:')
    col1, col2, col3, col4, col5 = st.columns(5)
    # Add a card to each column
    with col1:
        st.image(f"cards/{cards[0]}.jpg", use_column_width=True)
    with col2:
        st.image(f"cards/{cards[1]}.jpg", use_column_width=True)
    with col3:
        st.image(f"cards/{cards[2]}.jpg", use_column_width=True)
    with col4:
        st.image(f"cards/{cards[3]}.jpg", use_column_width=True)
    with col5:
        st.image(f"cards/{cards[4]}.jpg", use_column_width=True)

    st.write("")
    st.write("")
    st.subheader('Your objective is:')
    # Add a card to each column
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        st.image(f"cards/{cards[5]}.jpg", use_column_width=True)

def pick_cards(diff_label):
    # Create a list of cards with the specified probabilities
    if diff_label == 'Easy':
        cards = [i for i in range(1, 11) for _ in range(3)]
    if diff_label == 'Medium':
        cards = [i for i in range(1, 11) for _ in range(5)]
        cards += [i for i in range(11, 18)]
    if diff_label == 'Hard':
        cards = [i for i in range(1, 11) for _ in range(3)]
        cards += [i for i in range(11, 18) for _ in range(2)]
        cards += [i for i in range(18, 25)]
    # Shuffle the deck
    random.shuffle(cards)

    # Pick 6 cards from the deck
    return random.sample(cards, 6)

def find_solution(cards, max_trials=1000):
    nums = cards[:5]
    g1 = cards[5]
    ops = ['+', '-', '*', '/']
    exprs = []
    for nums_perm in itertools.permutations(nums):
        for ops_comb in itertools.product(ops, repeat=4):
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        for l in range(2):
                            if i + j + k + l == 3:
                                expr = f'({nums_perm[0]}{ops_comb[0]}{nums_perm[1]})' if i else f'{nums_perm[0]}{ops_comb[0]}{nums_perm[1]}'
                                expr = f'{expr}{ops_comb[1]}({nums_perm[2]}{ops_comb[2]}{nums_perm[3]})' if j else f'{expr}{ops_comb[1]}{nums_perm[2]}{ops_comb[2]}{nums_perm[3]}'
                                expr = f'({expr}){ops_comb[3]}{nums_perm[4]}' if l else f'{expr}{ops_comb[3]}{nums_perm[4]}'
                                # Check that a number is not subtracted from itself.
                                if '- ' not in expr and '-(' not in expr:
                                    try:
                                        result = eval(expr)
                                        if result == g1 and 0 not in nums_perm:
                                            return expr
                                    except:
                                        pass
                                    # Check if we have reached the maximum number of trials.
                                    if len(exprs) >= max_trials:
                                        return None
    return None

def find_cards_with_solution(diff_level):
    while True:
        cards = pick_cards(diff_level)
        solution = find_solution(cards)
        if solution != None:
          break
    
    return cards,solution

st.title('KRYPTO')
st.markdown("""
<style>
.rules-font {
    font-size:13px !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="rules-font">Six number-cards are dealt. One card is designated as the objective card. The object of the game is to combine all the remaining five cards in any order using any of the basic four arithmetic operations so that the result equals the objective. All 5 cards must be used exactly once. Once you figure out the solution, you can ask for another set. Enjoy! You can read about the origins of the game <a href="https://en.wikipedia.org/wiki/Krypto_(game)">here</a>. </p>', unsafe_allow_html=True)
st.markdown('<p class="rules-font">Created out of love of learning math by <a href="https://www.linkedin.com/in/amirgiveon/">Amir Give\'on</a> from <a href="https://www.neuron.vision">Neuron Vision</a>. </p>', unsafe_allow_html=True)


if "solution" not in st.session_state:
    st.session_state["solution"] = None

if "new_game" not in st.session_state:
    st.session_state["new_game"] = False

if "show_solution" not in st.session_state:
    st.session_state["show_solution"] = False

diff_levels = ['Easy','Medium','Hard']

cards_solutions = {}
for dl in diff_levels:
    with open(f'data/{dl}_cards_solutions.pkl', 'rb') as f:
            df = pickle.load(f)
    cards_solutions[dl] = df


diff_level = st.select_slider('Select difficulty level',options=diff_levels)
st.session_state["diff_level"] = diff_level

if st.button("Start a new game!"):
    st.session_state["new_game"] = True
    st.session_state["show_solution"] = False
    
    sample_row = cards_solutions[st.session_state["diff_level"]].sample(n=1)
    cards = sample_row['cards'].values[0]
    solution = sample_row['solution'].values[0]
    
    # cards,solution = find_cards_with_solution(st.session_state["diff_level"])
    st.session_state["solution"] = solution
    st.session_state["cards"] = cards
    display_cards(cards)

if st.session_state["new_game"] and st.button("I give up ???? Show me the solution"):
    st.session_state["show_solution"] = True
    
if st.session_state["new_game"] and st.session_state["show_solution"]:
    display_cards(st.session_state["cards"])
    st.subheader('One possible solution:')
    st.write(st.session_state["solution"])

# Print the session state to make it easier to see what's happening
# st.write(
#     f"""
#     ## Session state:
#     {st.session_state["new_game"]=}

#     {st.session_state["show_solution"]=}
#     """
# )

