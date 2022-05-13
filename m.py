import streamlit as st
import pydeck as pdk
import pandas as pd
import py_data

def app(key, values): 
    with st.spinner("Preparing map..."):

        us_data = py_data.get_data()

        lats = us_data['decimalLatitude']
        longs = us_data['decimalLongitude']
        mask = longs.isna() | lats.isna()
        mask = mask | us_data[key].isna()
        value_mask = us_data[key].isin(values)
        mask = mask | ~value_mask

        df = pd.DataFrame()
        df['lat'] = lats
        df['lon'] = longs

        df = df[~mask]
        if len(df) == 0:
            st.write("No latitude/longitude data found.")
        st.map(df)

    #TODO Filter out non-US (maybe)

# with st.spinner("Preparing data..."):
    # us_data = pd.read_parquet('final_data.parquet')

    # st.write(us_data.keys())

    # for key in us_data.keys():
        # if key == 'verbatimScientificName':
            # st.write(us_data[key])
        
    # lats = us_data['decimalLatitude']
    # longs = us_data['decimalLongitude']
    # mask = longs.isna() | lats.isna()


if __name__ == "__main__":
    app(names=[])
