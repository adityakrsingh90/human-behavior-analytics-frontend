import streamlit as st

def show():
    st.title("👋 Welcome to Human Behavior Analytics")
    st.caption("We’ll analyze your daily work patterns in a few simple steps")

    st.markdown("### What you’ll get:")
    st.markdown("""
    ✅ Productivity insights  
    ✅ Burnout risk detection  
    ✅ Personalized nudges  
    """)

    if st.button("🚀 Start Analysis"):
        st.session_state.onboarded = True
        st.rerun()
