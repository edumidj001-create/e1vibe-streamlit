import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="GLOBAL LPG INSIGHT", layout="wide")

def fetch_lpg_data():
    api_url = "https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=ODIzYjE5YjQ1ZWY1ZmJlZjQ1MjRiYTg0NzJmZTA4MzE=&itmId=Q029+&objL1=ALL&objL2=ALL&format=json&jsonVD=Y&prdSe=Y&startPrdDe=2000&endPrdDe=2024&orgId=101&tblId=DT_2AFF029"
    try:
        df = pd.DataFrame(requests.get(api_url).json())
        return df
    except:
        return None

st.title("🧭 GLOBAL LPG INSIGHT SYSTEM")
df = fetch_lpg_data()
if df is not None:
    st.dataframe(df.head(20))
