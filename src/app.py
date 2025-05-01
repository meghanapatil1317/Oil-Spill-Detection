import streamlit as st

import pandas as pd

# File paths
datafile = "CLEAN_AIS_2024_12_31.csv"
small_datafile = "TOP1000_AIS.csv"

st.header("Oil Spill Detection - AIS Data Mapping")

# Extract top 1000 rows and save to a new CSV
@st.cache_data
def extract_top_1000():
    try:
        df = pd.read_csv(datafile, nrows=1000)
        df.to_csv(small_datafile, index=False)
        return True
    except Exception as e:
        st.error(f"Error extracting top 1000 rows: {e}")
        return False

# Read the new CSV and prepare for mapping
@st.cache_data
def read_small_data():
    try:
        df = pd.read_csv(small_datafile)
        df = df.dropna(subset=['LAT', 'LON'])
        df.rename(columns={'LAT': 'latitude', 'LON': 'longitude'}, inplace=True)
        return df[['latitude', 'longitude']]
    except Exception as e:
        st.error(f"Error reading small dataset: {e}")
        return pd.DataFrame()

# Extract and visualize
if extract_top_1000():
    data = read_small_data()
    if not data.empty:
        
        st.map(data)
    else:
        st.warning("No data to display.")
