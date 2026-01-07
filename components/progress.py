import streamlit as st

def step_progress(step, total=3):
    st.progress(step/total)
