import streamlit as st
import pandas as pd
import data


def app(names): 
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


        lats = data.df['decimalLatitude']
        longs = data.df['decimalLongitude']
        mask = longs.isna() | lats.isna()
        mask = mask | data.df['scientificName'].isna()
        for name in names:
            mask = mask | ~data.df['scientificName'].str.contains(name)

        df = pd.DataFrame()
        df['lat'] = lats
        df['lon'] = longs

        df = df[~mask]
        st.map(df)

    #TODO Filter out non-US (maybe)





if __name__ == "__main__":
    app(names=[])
