import streamlit as st
import pandas as pd
import plotly.express as px
from utils import fetch_lpg_data
from style import apply_custom_style

st.set_page_config(page_title="Logistics LPG Insight", layout="wide")
apply_custom_style()

st.title("Logistics LPG Insight")
api_key = st.sidebar.text_input("🔑 OpenAPI 인증키", type="password")

if st.sidebar.button("데이터 불러오기") and api_key:
    df = fetch_lpg_data(api_key)
    if not df.empty:
        st.success("데이터 로드 완료")
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("데이터를 가져오지 못했습니다.")
