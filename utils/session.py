import streamlit as st

def set_session(token):
    st.session_state["token"] = token
    st.session_state["logged_in"] = True

def clear_session():
    st.session_state.clear()

def is_logged_in():
    return st.session_state.get("logged_in", False)
