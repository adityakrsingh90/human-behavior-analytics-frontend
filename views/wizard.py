import streamlit as st
from services.api import predict
from components.risk_badge import burnout_badge

def show():
    st.title("🧠 Daily Mental Check-in")
    st.caption("Answer honestly — this takes less than 30 seconds")

    if "step" not in st.session_state:
        st.session_state.step = 1

    # Progress bar
    progress = st.session_state.step / 4
    st.progress(progress)

    st.markdown("---")

    # STEP 1
    if st.session_state.step == 1:
        st.subheader("😴 How was your sleep?")
        sleep = st.slider(
            "Hours slept last night",
            0.0, 10.0, 6.5,
            help="Good sleep improves focus & reduces burnout"
        )

        if st.button("Next ➡️"):
            st.session_state.sleep = sleep
            st.session_state.step = 2
            st.rerun()

    # STEP 2
    elif st.session_state.step == 2:
        st.subheader("💻 Screen Exposure")
        screen = st.slider(
            "Total screen time today (hrs)",
            0.0, 15.0, 8.0,
            help="High screen time may increase fatigue"
        )

        if st.button("Next ➡️"):
            st.session_state.screen = screen
            st.session_state.step = 3
            st.rerun()

    # STEP 3
    elif st.session_state.step == 3:
        st.subheader("🎯 Focus Quality")
        focus = st.slider(
            "Focused work sessions",
            0, 10, 4,
            help="Deep focus sessions matter more than hours"
        )

        if st.button("Analyze My Day 🔍"):
            features = {
                "sleep_hours": st.session_state.sleep,
                "screen_time": st.session_state.screen,
                "focus_sessions": focus
            }

            with st.spinner("Analyzing patterns..."):
                res = predict(st.session_state.token, features)
                st.session_state.result = res.json()

            st.session_state.step = 4
            st.rerun()

    # STEP 4 – RESULT REVEAL
    else:
        data = st.session_state.result

        if "prediction" not in data:
            st.error("Something went wrong")
            return

        st.success("✅ Analysis Complete")
        st.markdown("### 🧠 Your Mental Snapshot")

        col1, col2, col3 = st.columns(3)

        col1.metric("⚡ Productivity", data["prediction"]["productivity_score"])
        col2.metric("🔥 Burnout Risk", data["prediction"]["burnout_score"])
        col3.metric("🧩 Archetype", data["prediction"]["archetype"])

        burnout_badge(data["prediction"]["burnout_score"])

        st.info(f"💡 **Personal Insight:** {data['nudge']}")

        st.markdown("---")

        if st.button("📊 View Dashboard"):
            st.session_state.completed = True
            st.session_state.step = 1
            st.rerun()
