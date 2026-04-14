import streamlit as st

def apply_custom_style():
    st.markdown(\"""
    <style>
    .metric-card { background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
    \"", unsafe_allow_html=True)
