import streamlit as st

st.title("Welcome to Streamlit !")
user_name = st.text_input("Please enter your Full Name in Capitals:")

if st.button("Greet Me"):
    st.write(f"Hello ! {user_name} ")
