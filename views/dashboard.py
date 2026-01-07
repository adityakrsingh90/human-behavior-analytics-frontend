import streamlit as st
from services.api import predict
from components.risk_badge import burnout_badge


def show():
    st.title("📊 Productivity & Burnout Dashboard")
    st.caption("Analyze your work patterns and mental load")

    st.markdown("---")

    # 🔹 INPUT SECTION
    col1, col2, col3 = st.columns(3)

    with col1:
        sleep = st.slider("😴 Sleep Hours", 0.0, 10.0, 6.5)

    with col2:
        screen = st.slider("💻 Screen Time (hrs)", 0.0, 15.0, 8.0)

    with col3:
        focus = st.slider("🎯 Focus Sessions", 0, 10, 4)

    st.markdown("")

    # 🔍 ANALYZE BUTTON
    if st.button("🔍 Analyze My Behavior"):
        features = {
            "sleep_hours": sleep,
            "screen_time": screen,
            "focus_sessions": focus
        }

        with st.spinner("Analyzing your behavior..."):
            res = predict(st.session_state["token"], features)
            data = res.json()

        # ❌ API ERROR HANDLING
        if "prediction" not in data:
            st.error("Prediction failed")
            st.write(data)
            return

        st.markdown("---")
        st.subheader("🧠 Your Insights")

        # 🔹 METRICS
        m1, m2, m3 = st.columns(3)

        m1.metric(
            "⚡ Productivity Score",
            data["prediction"]["productivity_score"]
        )

        m2.metric(
            "🔥 Burnout Risk",
            data["prediction"]["burnout_score"]
        )

        m3.metric(
            "🧩 Archetype",
            data["prediction"]["archetype"]
        )

        st.markdown("")

        # 🎨 COLOR-CODED RISK BADGE (✅ CORRECT PLACE)
        burnout_badge(data["prediction"]["burnout_score"])

        # 💡 NUDGE
        st.info(f"💡 **Smart Nudge:** {data['nudge']}")
