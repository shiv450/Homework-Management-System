import streamlit as st

st.subheader("All Added Homework:")

with open("homework.txt", "r")as f:
    x = f.read()
    st.write(x)

st.page_link("homepage.py")