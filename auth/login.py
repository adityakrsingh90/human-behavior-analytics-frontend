import streamlit as st
from services.api import login
from utils.session import set_session

def show():
    st.title("🔐 Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        res = login(email, password)

        data = res.json()

        if res.status_code == 200:
            token = data.get("access_token")

            if not token:
                st.error("Login failed: token not found")
                st.write(data)  # debug
                return

            set_session(token)
            st.success("Login successful")
            st.rerun()
        else:
            st.error(data.get("detail", "Invalid credentials"))
