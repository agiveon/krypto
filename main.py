import streamlit as st
import pandas as pd
import numpy as np
from google.oauth2 import service_account
import gspread
import datetime
import requests
import pickle

CARD_WIDTH = 200

col1, col2, col3, col4, col5 = st.beta_columns(5)

# Add a card to each column
with col1:
    st.title("Card 1")
    st.image("cards/1.jpg", width=CARD_WIDTH)

with col2:
    st.title("Card 2")
    st.image("cards/1.jpg", width=CARD_WIDTH)

with col3:
    st.title("Card 3")
    st.image("cards/1.jpg", width=CARD_WIDTH)

with col4:
    st.title("Card 4")
    st.image("cards/1.jpg", width=CARD_WIDTH)

with col5:
    st.title("Card 5")
    st.image("cards/1.jpg", width=CARD_WIDTH)
