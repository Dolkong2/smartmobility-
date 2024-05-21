import streamlit as st
option = st.selectbox(
    "좋아 하는 동물은?",
    ("Email", "Home phone", "Mobile phone"))

st.write("You selected:", option)