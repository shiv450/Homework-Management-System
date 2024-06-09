import streamlit as st
import datetime as dt

#we create a list of all the lines in the file called...lines
with open("homework.txt" , "r") as f:
    lines = f.readlines()
    #we take the date of which line they want
date = st.text_input("Enter the date of the homework you want to change(dd-mm):")
    #
for i in range(len(lines)):
    line = lines[i].split(">")

    if line[0] == date:
        st.write("Old hw :" + line[1])
        homework = st.text_input(date+">")

        if homework != "":
            lines[i] = line[0]+">"+homework+"\n"
        

with open ("homework.txt", "w") as f:
    f.writelines(lines)
    print("Homework sucsessfuly updated")

st.page_link("homepage.py")