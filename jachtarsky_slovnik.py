import pandas as pd
import streamlit as st
import random
import time

def change_choice_strategy():
    st.session_state.i = -1

st.title('Jachtársky slovník')
ord = st.radio("Poradie skúšania", options=["porade","náhodne"], on_change=change_choice_strategy)

def get_row():
    if ord=='porade':
        if 'i' not in st.session_state:
            st.session_state['i'] = -1
        st.session_state.i += 1
        return st.session_state.s.iloc[st.session_state.i]
    return st.session_state.s.iloc[random.randint(0, len(st.session_state.s)-1)]

if 's' not in st.session_state:
    st.session_state['s'] = pd.read_csv("jachtarsky_slovnik2.csv", header=None, names=["eng","svk"], sep="\t")
    st.session_state['r'] = get_row()
    st.session_state.eng_text = st.session_state.r['eng']
    st.session_state.svk_text = ''
    st.session_state['i'] = -1

eng_text = st.text_area('English',key='eng_text')
svk_text = st.text_area('Slovak', key='svk_text')

def show_translation():    
    st.session_state.svk_text = st.session_state.r['svk']

def next_word():
    st.session_state.r = get_row()
    st.session_state.svk_text = ''
    st.session_state.eng_text = st.session_state.r['eng']

translate_button = st.button('Translate',key="translate_button", on_click=show_translation)
next_button = st.button('Next',key="next_button", on_click=next_word)