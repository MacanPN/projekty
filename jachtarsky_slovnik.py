import pandas as pd
import streamlit as st
import random

def change_choice_strategy():
    st.session_state.i = int(st.session_state.co)
    st.session_state.r = st.session_state.s.iloc[st.session_state.i]
    st.session_state.eng_text = st.session_state.r['eng']
    st.session_state.svk_text = ''


st.title('Jachtársky slovník')

def get_row():
    if ord=='porade':
        if 'i' not in st.session_state:
            st.session_state['i'] = -1
        st.session_state.i += 1
    else:
        st.session_state.i = random.randint(0, len(st.session_state.s)-1)
    st.session_state.co = st.session_state.i
    return st.session_state.s.iloc[st.session_state.i]

if 's' not in st.session_state:
    st.session_state['s'] = pd.read_csv("jachtarsky_slovnik2.csv", header=None, names=["eng","svk"], sep="\t")
    st.session_state['r'] = get_row()
    st.session_state.eng_text = st.session_state.r['eng']
    st.session_state.svk_text = ''
    st.session_state['i'] = -1

ord = st.radio("Poradie skúšania", options=["porade","náhodne"], on_change=change_choice_strategy)
num = st.number_input("Cislo otazky", format="%d", step=1, key="co", on_change=change_choice_strategy)
eng_text = st.text_area('English',key='eng_text')
svk_text = st.text_area('Slovak', key='svk_text')

def show_translation():    
    st.session_state.svk_text = st.session_state.r['svk']

def next_word():
    st.session_state.r = get_row()
    st.session_state.svk_text = ''
    st.session_state.eng_text = st.session_state.r['eng']

def add_word_to_vocabulary():
    st.session_state.vocab += "\n"+" : ".join(st.session_state.r)

col1, col2, col3 = st.columns([1,1,1])
with col1:
    translate_button = st.button('Translate',key="translate_button", on_click=show_translation)
with col2:
    next_button = st.button('Next',key="next_button", on_click=next_word)
with col3:
    vocab_button = st.button('Do slovníka', on_click=add_word_to_vocabulary)

vocab = st.text_area('Váš slovník', key='vocab')
