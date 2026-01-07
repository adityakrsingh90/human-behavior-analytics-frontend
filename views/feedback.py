import streamlit as st
from services.api import send_feedback

def show():
    st.header("🗣️ Prediction Feedback")

    prediction_id = st.text_input("Prediction ID")
    accurate = st.radio("Was prediction accurate?", [True, False])

    if st.button("Submit Feedback"):
        send_feedback(
            st.session_state["token"],
            {
                "prediction_id": prediction_id,
                "is_accurate": accurate
            }
        )
        st.success("Feedback submitted")
