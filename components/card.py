import streamlit as st

def card(title, subtitle=""):
    st.markdown(f"""
    <div style="
        background:#0f172a;
        border:1px solid #1e293b;
        border-radius:16px;
        padding:24px;
        margin-bottom:16px;">
        <h3 style="margin:0 0 6px 0;">{title}</h3>
        <p style="opacity:.7;margin:0;">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)
