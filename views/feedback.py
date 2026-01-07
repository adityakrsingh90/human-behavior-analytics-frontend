import streamlit as st
from services.api import send_feedback


def show():
    st.title("💬 Share Your Feedback")
    st.caption("Help us improve our predictions")

    name = st.text_input("Your Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone (optional)")

    st.subheader("Prediction Accuracy")
    accuracy = st.radio(
        "Was the prediction accurate?",
        ["Yes", "Partially", "No"]
    )

    accuracy_map = {
        "Yes": True,
        "No": False,
        "Partially": None
    }

    rating = st.slider("How helpful was the prediction?", 1, 5, 3)

    feedback = st.text_area(
        "Additional Feedback / Suggestions",
        placeholder="Tell us what worked well or what can be improved..."
    )

    if st.button("Submit Feedback"):
        if not name or not email:
            st.error("Name and Email are required")
            return

        payload = {
            "name": name,
            "email": email,
            "phone": phone,
            "is_accurate": accuracy_map[accuracy],
            "rating": rating,
            "feedback": feedback
        }

        res = send_feedback(payload)

        if res.status_code == 200:
            st.success("🙏 Thank you for your feedback!")
            st.balloons()
        else:
            st.error("Failed to submit feedback")
