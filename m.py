import streamlit as st
import pandas as pd


us_data = pd.read_parquet('final_data.parquet')
lats = us_data['decimalLatitude']
longs = us_data['decimalLongitude']
mask = longs.isna() | lats.isna()

df = pd.DataFrame()
df['lat'] = lats
df['lon'] = longs

df = df[~mask]
st.map(df, zoom=9)

#TODO Filter out non-US (maybe)
