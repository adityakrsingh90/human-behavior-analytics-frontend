import streamlit as st

def theme_toggle():
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"

    toggle = st.sidebar.toggle("🌙 Dark Mode", value=True)

    st.session_state.theme = "dark" if toggle else "light"
