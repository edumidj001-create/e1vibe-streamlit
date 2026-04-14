import requests
import pandas as pd
import streamlit as st

SUPABASE_URL = "https://imfehrrklgsfefmsoxws.supabase.co"
SUPABASE_KEY = "sb_publishable_Jy5Z2X_nKPgCIEasjweQDA_N4wcsqDp"

def fetch_visit_logs():
    headers = {"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}"}
    url = f"{SUPABASE_URL}/rest/v1/visitlog?select=*"
    try:
        response = requests.get(url, headers=headers)
        return pd.DataFrame(response.json())
    except:
        return pd.DataFrame()

def filter_data(df, search_query=None, region=None, sigungu=None, station_name=None):
    return df # Simplified for push
