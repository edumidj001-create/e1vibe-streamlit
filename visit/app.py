import streamlit as st
import pandas as pd
import plotly.express as px
from utils import fetch_visit_logs, filter_data
from style import apply_visit_style, render_metric_card

st.set_page_config(page_title="E1 Visit Log Insights", layout="wide")
apply_visit_style()

st.header("📋 E1 방문일지 분석 대시보드")
df = fetch_visit_logs()

if not df.empty:
    st.dataframe(df.head(50), use_container_width=True)
    # Charts and filters...
else:
    st.error("데이터 로드 실패")
