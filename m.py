import streamlit as st
import pandas as pd

def app(df): 
    with st.spinner("Preparing map..."):
        # st.pydeck_chart(pdk.Deck(
        # map_style='mapbox://styles/mapbox/light-v9',
        # initial_view_state=pdk.ViewState(
        #     latitude=37.76,
        #     longitude=-122.4,
        #     zoom=11,
        #     pitch=50,
        # ),
        # layers=[
        #     pdk.Layer(
        #         'HexagonLayer',
        #         data=df,
        #         get_position='[lon, lat]',
        #         radius=200,
        #         elevation_scale=4,
        #         elevation_range=[0, 1000],
        #         pickable=True,
        #         extruded=True,
        #     ),
        #     pdk.Layer(
        #         'ScatterplotLayer',
        #         data=df,
        #         get_position='[lon, lat]',
        #         get_color='[200, 30, 0, 160]',
        #         get_radius=200,
        #     ),
        # ],
        # ))
        st.map(df)

    #TODO Filter out non-US (maybe)


df = None

with st.spinner("Preparing data..."):
    us_data = pd.read_parquet('final_data.parquet')
    lats = us_data['decimalLatitude']
    longs = us_data['decimalLongitude']
    mask = longs.isna() | lats.isna()

    df = pd.DataFrame()
    del us_data
    df['lat'] = lats
    df['lon'] = longs

    df = df[~mask]

app(df)

