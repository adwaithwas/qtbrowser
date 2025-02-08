import streamlit as st
import random as r

st.set_page_config(page_title="qt browser", layout="centered", page_icon="")

st.title("Search")

barText = ["what are you searching today", "youtube? or twitch? what one is today?", "type on me please"]
bar = st.text_input(barText[r.randint(0,2)])

if st.button("search"):
    t.write("searching") #placeholder for searching