import streamlit as st
from services.api import signup, resend_verification_email
import re


# -------------------------------
# PASSWORD STRENGTH CHECK
# -------------------------------
def password_strength(password: str):
    if len(password) < 6:
        return "Weak", "🔴"

    score = 0
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    if score <= 1:
        return "Weak", "🔴"
    elif score == 2:
        return "Medium", "🟡"
    else:
        return "Strong", "🟢"


# -------------------------------
# SIGNUP UI
# -------------------------------
def show():
    st.title("📝 Signup")
    st.caption("Create your account in less than a minute")

    # session state
    if "signup_success" not in st.session_state:
        st.session_state.signup_success = False
    if "signup_email" not in st.session_state:
        st.session_state.signup_email = ""

    email = st.text_input("Email", value=st.session_state.signup_email)

    password = st.text_input(
        "Password",
        type="password",
        help="At least 6 characters. Use letters, numbers & symbols."
    )

    # 🔐 Password rule
    st.caption("🔒 Password must be at least 6 characters")

    # 🔋 Password strength (only while typing)
    if password:
        strength, icon = password_strength(password)
        st.write(f"**Password strength:** {icon} {strength}")

    # -------------------------------
    # CREATE ACCOUNT
    # -------------------------------
    if st.button("Create Account"):
        if not email:
            st.error("📧 Email is required.")
            return

        if len(password) < 6:
            st.error("🔒 Password must be at least 6 characters long.")
            return

        res = signup(email, password)

        try:
            data = res.json()
        except ValueError:
            data = {}

        if res.status_code == 200:
            st.session_state.signup_success = True
            st.session_state.signup_email = email

            st.success("✅ Account created successfully!")
            st.balloons()

        else:
            error = data.get("detail", "Signup failed")

            if "password" in error.lower():
                st.error("🔒 Password must be at least 6 characters.")
            elif "email" in error.lower():
                st.error("📧 Please enter a valid email address.")
            elif "already" in error.lower():
                st.error("⚠️ Account already exists. Please login.")
            else:
                st.error(error)

    # -------------------------------
    # POST-SIGNUP (ONLY AFTER SUCCESS)
    # -------------------------------
    if st.session_state.signup_success:
        st.info("📧 We’ve sent you a verification email. Please verify before logging in.")

        if st.button("🔄 Resend verification email"):
            resend_verification_email(st.session_state.signup_email)
            st.success("📨 Verification email sent again.")
