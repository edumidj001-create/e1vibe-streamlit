import streamlit as st

def apply_visit_style():
    st.markdown(\"""
    <style>
    .stApp { background: #f8fafc; }
    </style>
    \"", unsafe_allow_html=True)

def render_metric_card(label, value, delta=None, direction="up"):
    st.metric(label, value, delta)
