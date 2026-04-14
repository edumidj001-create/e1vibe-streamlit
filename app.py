import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from utils import load_data, get_data_summary, get_descriptive_stats, get_correlation_matrix
import io
import time

# 페이지 설정
st.set_page_config(
    page_title="Precision Curator | Excel Insight Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Look
st.markdown(\"""
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Outfit:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Sidebar Background & Style */
    [data-testid="stSidebar"] {
        background-color: #F8F9FA;
        border-right: 1px solid #E9ECEF;
    }

    /* Main Content Background */
    [data-testid="stAppViewContainer"] {
        background-color: #FFFFFF;
    }

    /* Sidebar Branding */
    .sidebar-brand {
        padding: 1.5rem 0;
        text-align: left;
    }
    .brand-title {
        font-family: 'Outfit', sans-serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: #1A1A1A;
        margin-bottom: 0;
    }
    .brand-subtitle {
        font-size: 0.8rem;
        color: #6C757D;
    }

    /* Red Button Style for Upload */
    .stButton > button {
        width: 100%;
        background-color: #D32F2F;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.6rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #B71C1C;
        border: none;
        color: white;
        transform: translateY(-2px);
    }

    /* Metric Cards */
    .metric-card {
        background-color: #FFFFFF;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #D32F2F;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
    }
    .metric-title {
        font-size: 0.75rem;
        font-weight: 700;
        color: #D32F2F;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .metric-value {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1A1A1A;
        margin-top: 5px;
    }
    .metric-delta {
        font-size: 0.8rem;
        color: #2E7D32;
        margin-top: 5px;
    }

    /* Insights Box */
    .insight-box {
        background-color: #FFF5F5;
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid #FFCDD2;
        margin-top: 1rem;
    }
    .insight-title {
        font-weight: 700;
        color: #C62828;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .insight-content {
        font-size: 0.9rem;
        color: #424242;
        margin-top: 10px;
    }
</style>
\"", unsafe_allow_html=True)

if 'data' not in st.session_state:
    st.session_state.data = None
if 'page' not in st.session_state:
    st.session_state.page = "Overview"

with st.sidebar:
    st.markdown(f\"\""
    <div class="sidebar-brand">
        <div class="brand-title">Precision Curator</div>
        <div class="brand-subtitle">Data Narrative Engine</div>
    </div>
    \"\"", unsafe_allow_html=True)
    st.write("---")
    pages = ["Overview", "Statistics", "Visualization"]
    for p in pages:
        icon = "🏠" if p == "Overview" else ("📊" if p == "Statistics" else "📈")
        if st.button(f"{icon} {p}", key=f"nav_{p}", use_container_width=True):
            st.session_state.page = p
            st.rerun()

    st.write("---")
    uploaded_file = st.file_uploader("Upload File", type=['csv', 'xlsx', 'xls'])
    
    if uploaded_file is not None:
        try:
            st.session_state.data = load_data(uploaded_file)
            st.success("File uploaded successfully!")
        except Exception as e:
            st.error(f"Error: {e}")

if st.session_state.data is not None:
    df = st.session_state.data
    if st.session_state.page == "Overview":
        st.header("Project Overview")
        # Overview logic here
        st.dataframe(df.head(20), use_container_width=True)
    elif st.session_state.page == "Statistics":
        st.header("Statistical Analysis")
        stats = get_descriptive_stats(df)
        if stats is not None:
            st.dataframe(stats, use_container_width=True)
    elif st.session_state.page == "Visualization":
        st.header("Visualization")
        # Chart logic here
        st.info("시각화 준비 완료")
else:
    st.title("Welcome to Precision Curator")
    st.info("분석을 위해 파일을 업로드해 주세요.")
