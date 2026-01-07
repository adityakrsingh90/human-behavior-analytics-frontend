import streamlit as st

def burnout_badge(score):
    if score < 0.4:
        st.success("🟢 Low Burnout Risk")
    elif score < 0.7:
        st.warning("🟡 Moderate Burnout Risk")
    else:
        st.error("🔴 High Burnout Risk")
