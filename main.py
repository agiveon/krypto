import streamlit as st
import pandas as pd
import numpy as np
from google.oauth2 import service_account
import gspread
import datetime
import requests
import pickle

CARD_WIDTH = 100

col1, col2, col3, col4, col5 = st.columns(5)

# Add a card to each column
with col1:
    st.image("cards/1.jpg", width=CARD_WIDTH)
with col2:
    st.image("cards/1.jpg", width=CARD_WIDTH)
with col3:
    st.image("cards/1.jpg", width=CARD_WIDTH)
with col4:
    st.image("cards/1.jpg", width=CARD_WIDTH)
with col5:
    st.image("cards/1.jpg", width=CARD_WIDTH)

with st.container():
    st.title("Goal:")
    st.image("cards/1.jpg", width=CARD_WIDTH*2, use_column_width=False)

# Center the last card using CSS
st.markdown(
    """
    <style>
        .stImage > img {
            max-width: 100%;
            display: block;
            margin: auto;
        }
    </style>
    """,
    unsafe_allow_html=True
)