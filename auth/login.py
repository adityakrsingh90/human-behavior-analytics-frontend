import streamlit as st
from services.api import login, resend_verification_email
from utils.session import set_session


def show():
    st.title("🔐 Login")
    st.caption("Login to continue")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.query_params.get("type") == "signup":
        st.success("✅ Your email has been verified. Please login.")


    if st.button("Login"):
        res = login(email, password)

        # ✅ SAFE JSON PARSE
        try:
            data = res.json()
        except ValueError:
            data = {}

        # ✅ SUCCESS
        if res.status_code == 200:
            token = data.get("access_token")
            if not token:
                st.error("Login failed.")
                return

            set_session(token)
            st.success("✅ Login successful")
            st.balloons()   # 🎉 delight
            st.rerun()

        # ❌ ERROR CASES
        else:
            detail = data.get("detail", "").lower()

            # 🔴 EMAIL NOT VERIFIED
            if "confirm" in detail or "verify" in detail:
                st.error("📧 Please verify your email before logging in.")

                if st.button("🔄 Resend verification email"):
                    resend_verification_email(email)
                    st.success("Verification email sent again.")

            else:
                st.error("Invalid email or password")
