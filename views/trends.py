import streamlit as st
import pandas as pd

def show():
    st.title("📈 Your Progress")
    st.caption("Consistency matters more than perfection")

    df = pd.DataFrame({
        "Day": ["Mon","Tue","Wed","Thu","Fri"],
        "Productivity": [0.55,0.6,0.68,0.72,0.7],
        "Burnout": [0.6,0.55,0.48,0.4,0.42]
    })

    st.line_chart(df.set_index("Day"))

    st.success("⬆️ Productivity is improving this week")
