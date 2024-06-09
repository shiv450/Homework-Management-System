import streamlit as st
import datetime as dt

#here we get todays date
today = dt.datetime.today()

#now, we take the input for the hw 
homework = st.text_input(today.strftime("Enter hw for %d-%m-%A:"))

if homework != "":

    #here we put the date in a dd-mm, like - 18-10(8rth octuber)
    day = today.strftime("%d-%m> ")

    homework = day+homework

    #we open the file with appened mode and write the homework after leaving one line
    with open("homework.txt", "a")as f:
        f.write(f"\n{homework}")
    st.write("Homework added")

st.page_link("homepage.py")