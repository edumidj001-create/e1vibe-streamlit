import requests
import pandas as pd
import streamlit as st

def fetch_lpg_data(api_key):
    url = "http://data.ex.co.kr/openapi/business/lpgServiceAreaInfo"
    params = {"key": api_key, "type": "json"}
    try:
        response = requests.get(url, params=params, timeout=15)
        data = response.json()
        if data.get("list"):
            return pd.DataFrame(data["list"])
        return pd.DataFrame()
    except:
        return pd.DataFrame()
