import streamlit as st
from services.api import signup


def show():
    st.title("📝 Signup")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Create Account"):
        res = signup(email, password)
        if res.status_code == 200:
            st.success("Account created. Please login.")
        else:
            st.error("Signup failed")
