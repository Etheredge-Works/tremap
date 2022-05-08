import streamlit as st
import pandas as pd

st.title("Tree")

import requests

def app():
    url = "https://api.opentreeoflife.org/v3/"


    # r = requests.get(url + "taxonomy/", params={"ott_id": "ott_node:1"})
    df = pd.read_parquet("final_data.parquet")
    st.write(df.columns)

    # r = requests.get(url + "tnrs/autocomplete", params={"query": "")
    st.write(r.json())

if __name__ == "__main__":
    app()
    