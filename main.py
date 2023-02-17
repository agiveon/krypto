import streamlit as st
import pandas as pd
import numpy as np
from google.oauth2 import service_account
import random


CARD_WIDTH = 100

st.subheader('Use all these cards:')
col1, col2, col3, col4, col5 = st.columns(5)
# Add a card to each column
with col1:
    st.image("cards/1.jpg", width=CARD_WIDTH)
with col2:
    st.image("cards/2.jpg", width=CARD_WIDTH)
with col3:
    st.image("cards/3.jpg", width=CARD_WIDTH)
with col4:
    st.image("cards/4.jpg", width=CARD_WIDTH)
with col5:
    st.image("cards/5.jpg", width=CARD_WIDTH)


st.write("")
st.write("")
st.subheader('to reach:')
# Add a card to each column
col1, col2, col3, col4, col5 = st.columns(5)
with col3:
    st.image("cards/6.jpg", width=CARD_WIDTH)

