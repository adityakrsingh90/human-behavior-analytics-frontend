import streamlit as st
from services.api import explain

def show():
    st.header("🔍 Explain Prediction")
    st.write("explain page loaded")

    features = {
        "sleep_hours": st.number_input("Sleep Hours", 0.0, 10.0, 6.0),
        "screen_time": st.number_input("Screen Time", 0.0, 15.0, 8.0)
    }

    if st.button("Explain"):
        res = explain(st.session_state["token"], features)
        explanation = res.json()["explanation"]

        for k, v in explanation.items():
            st.write(f"**{k}** → {v}")
