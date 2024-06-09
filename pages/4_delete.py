import streamlit as st
import datetime as dt


with open("homework.txt" , "r") as f:
    lines = f.readlines()
date = st.text_input("enter the date of the homework you want to delete(dd-mm):")
for i in range(len(lines)):
    line = lines[i].split(">")

    if line[0] == date:
        lines[i] = ""
        with open ("homework.txt" , "w") as f:
            f.writelines(lines)
        st.write("homework you deleted-  " + line[1])

st.page_link("homepage.py")