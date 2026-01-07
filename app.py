import streamlit as st

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Auth
from auth import login, signup

# Views
from views import (
    onboarding,
    wizard,
    dashboard,
    trends,
    explain,
    feedback
)

# Utils
from utils.session import is_logged_in, clear_session


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Human Behavior Analytics",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# SESSION DEFAULTS
# --------------------------------------------------
if "onboarded" not in st.session_state:
    st.session_state.onboarded = False

if "completed" not in st.session_state:
    st.session_state.completed = False

if "auth_mode" not in st.session_state:
    st.session_state.auth_mode = "login"   # login | signup


# --------------------------------------------------
# AUTH FLOW (NO RADIO, CTA BASED)
# --------------------------------------------------
if not is_logged_in():

    st.sidebar.title("🔐 Authentication")

    # Centered auth container
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:

        if st.session_state.auth_mode == "login":
            login.show()

            st.markdown("---")
            st.caption("🆕 New user?")
            if st.button("Create an account"):
                st.session_state.auth_mode = "signup"
                st.rerun()

        else:
            signup.show()

            st.markdown("---")
            st.caption("🔐 Already have an account?")
            if st.button("Back to Login"):
                st.session_state.auth_mode = "login"
                st.rerun()


# --------------------------------------------------
# ONBOARDING (FIRST LOGIN ONLY)
# --------------------------------------------------
elif not st.session_state.onboarded:
    onboarding.show()

# --------------------------------------------------
# STEP-BY-STEP WIZARD
# --------------------------------------------------
elif not st.session_state.completed:
    wizard.show()

# --------------------------------------------------
# MAIN APPLICATION
# --------------------------------------------------
else:
    st.sidebar.title("🧭 Navigation")

    page = st.sidebar.radio(
        "Go to",
        ["Dashboard", "Trends", "Explain", "Feedback", "Logout"]
    )

    if page == "Dashboard":
        dashboard.show()

    elif page == "Trends":
        trends.show()

    elif page == "Explain":
        explain.show()

    elif page == "Feedback":
        feedback.show()

    else:  # Logout
        clear_session()
        st.session_state.onboarded = False
        st.session_state.completed = False
        st.session_state.auth_mode = "login"
        st.rerun()
