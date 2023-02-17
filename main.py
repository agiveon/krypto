import streamlit as st
import pandas as pd
import numpy as np
from google.oauth2 import service_account
import random
import itertools

st.write('''<style>

[data-testid="column"] {
    width: calc(20% - 1rem) !important;
    flex: 1 1 calc(20% - 1rem) !important;
    min-width: calc(20% - 1rem) !important;
}
</style>''', unsafe_allow_html=True)

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
    st.subheader('to reach:')
    # Add a card to each column
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        st.image(f"cards/{cards[5]}.jpg", use_column_width=True)

def pick_cards():
    # Create a list of cards with the specified probabilities
    cards = [i for i in range(1, 11) for _ in range(3)]
    cards += [i for i in range(11, 18) for _ in range(2)]
    cards += [i for i in range(18, 25)]

    # Shuffle the deck
    random.shuffle(cards)

    # Pick 6 cards from the deck
    return random.sample(cards, 6)

def find_solution(cards, max_trials=1000):
    # Generate all possible permutations of the 5 integers and all possible
    # combinations of the basic arithmetic operations.
    nums = cards[:5]
    goal = cards[5]
    ops = ['+', '-', '*', '/']
    exprs = []
    for nums_perm in itertools.permutations(nums):
        for ops_comb in itertools.product(ops, repeat=4):
            # Try all possible combinations of parentheses.
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        for l in range(2):
                            if i + j + k + l == 3:
                                expr = f'({nums_perm[0]}{ops_comb[0]}{nums_perm[1]})' if i == 1 else f'{nums_perm[0]}{ops_comb[0]}{nums_perm[1]}'
                                expr = f'({expr}{ops_comb[1]}{nums_perm[2]})' if j == 1 else f'{expr}{ops_comb[1]}{nums_perm[2]}'
                                expr = f'({nums_perm[3]}{ops_comb[2]}{nums_perm[4]})' if l == 1 else f'{nums_perm[3]}{ops_comb[2]}{nums_perm[4]}'
                                expr = f'({expr}{ops_comb[3]})' if k == 1 else f'{expr}{ops_comb[3]}'
                                # Evaluate the expression and see if it equals g1.
                                try:
                                    result = eval(expr)
                                    if result == goal:
                                        return expr
                                except:
                                    pass
            # Check if we have reached the maximum number of trials.
            if len(exprs) >= max_trials:
                break
        if len(exprs) >= max_trials:
            break
    
    # If no expression is found, return None.
    return None

def find_cards_with_solution():
    solotion = None
    while not solotion:
        cards = pick_cards()
        solution = find_solution(cards)
    return cards,solution


if "new_game" not in st.session_state:
    st.session_state["new_game"] = False

if "show_solution" not in st.session_state:
    st.session_state["show_solution"] = False

if st.button("new_game"):
    st.session_state["new_game"] = True
    st.session_state["show_solution"] = False
    cards,solution = find_cards_with_solution()
    st.session_state["cards"] = cards
    display_cards(cards)

if st.session_state["new_game"] and st.button("show_solution"):
    st.session_state["show_solution"] = True
    
if st.session_state["new_game"] and st.session_state["show_solution"]:
    display_cards(st.session_state["cards"])
    st.write("solution")

# Print the session state to make it easier to see what's happening
# st.write(
#     f"""
#     ## Session state:
#     {st.session_state["new_game"]=}

#     {st.session_state["show_solution"]=}
#     """
# )

