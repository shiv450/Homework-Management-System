import streamlit as st


st.header("Welcome to the Homework Mangement System")

import datetime as dt


#here we try to open homework.txt, if it doesn't exist, then we make one
try:
    with open("homework.txt", "r")as f:
        pass
except:
    with open("homework.txt", "w") as f:
        f.write("")
        print("homework.txt did not exist, the HMS has created one for you")

#this is for the first option, add new hw

st.subheader("What do you want to do today?")
st.page_link("pages/1_add.py")
st.page_link("pages/2_view.py")
st.page_link("pages/3_edit.py")
st.page_link("pages/4_delete.py")
