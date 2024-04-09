import pandas as pd
import streamlit as st
import random
import time

def get_random_row():
    return st.session_state.s.iloc[random.randint(0, len(st.session_state.s)-1)]

if 's' not in st.session_state:
    st.session_state['s'] = pd.read_csv("jachtarsky_slovnik2.csv", header=None, names=["eng","svk"], sep="\t")
    st.session_state['r'] = get_random_row()
    st.session_state.eng_text = st.session_state.r['eng']
    st.session_state.svk_text = ''

st.title('Translation App')

eng_text = st.text_area('English',key='eng_text')
svk_text = st.text_area('Slovak', key='svk_text')

def show_translation():    
    st.session_state.svk_text = st.session_state.r['svk']

def next_word():
    st.session_state.r = get_random_row()
    st.session_state.svk_text = ''
    st.session_state.eng_text = st.session_state.r['eng']

translate_button = st.button('Translate',key="translate_button", on_click=show_translation)
next_button = st.button('Next',key="next_button", on_click=next_word)