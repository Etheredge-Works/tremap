import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

import gbif
import inat
import py_data as downloaded_data

def app():
    st.title("Exploration")

    st.write("Hello Streamlit!")
    df = downloaded_data.get_data()
    images = df['identifier']
    ids = df['gbifID'].to_list()[:10]
    with st.spinner("Loading..."):
        datas = gbif.get_ny_species(ids)
    st.write(datas[:4])

    st.write("# break")
    st.image(images.to_list()[:10])

    with st.spinner("Loading..."):
        d = gbif.get_ny_species()

    options = ["Option 1", "Option 2", "Option 3"]
    options += gbif.get_species()

    # choice1 = st.multiselect("Select species (suggest):", gbif.suggest(""))
    # choice = st.multiselect("Select species:", options)
    txt = st.text_input("Enter a species name to search for:")
    with st.spinner("Loading..."):
        data = gbif.api_suggest(txt)
    choice = st.selectbox("Select species (suggest):", data, format_func=lambda x: x["scientificName"])
    # choice = st.selectbox("Select species (suggest):", gbif.get_s_names(data))
    st.write("## Choice")
    st.write(choice)

    st.write("## Gotten Data Choice")
    with st.spinner("Loading..."):
        item = gbif.get_item(choice["key"])
    st.write(item)

    st.write("## Get Media")
    images = gbif.get_media(item['key'])
    if images:
        st.write(images)
        images = [x['identifier'] for x in images['results']]
        st.image(images)
    else:
        st.write("No images found")

    def formatter(x):
        type = x['type']
        name = x.get('name', 'NO NAME')
        return f"{type} - {name}"
    inat_r = inat.get_results(choice["scientificName"])
    st.write("## INAT Results")
    if inat_r['total_results'] > 0:
        st.write(inat_r)
        st.image(inat.get_default_image(inat_r, limit=10))
        st.write("## INAT Taxon Photos")
        inat_choice = st.selectbox(
            "Select INAT species:", 
            inat_r['results'],
            # format_func=formatter
            format_func=lambda x: f"{x['type']}: {x['record']['name']}"
        )
        st.image(inat.get_taxon_images_b(inat_choice, limit=10))

        # st.write("## INAT Images")
        # i = inat.get_taxon_images(inat_r, limit=10)
        #
        # st.image(i)


# st.write("## DF")
# st.dataframe(gbif.get_item(choice["key"]))



# st.


# df = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.pydeck_chart(pdk.Deck(
#      map_style='mapbox://styles/mapbox/light-v9',
#      initial_view_state=pdk.ViewState(
#          latitude=37.76,
#          longitude=-122.4,
#          zoom=11,
#          pitch=50,
#      ),
#      layers=[
#          pdk.Layer(
#             'HexagonLayer',
#             data=df,
#             get_position='[lon, lat]',
#             radius=200,
#             elevation_scale=4,
#             elevation_range=[0, 1000],
#             pickable=True,
#             extruded=True,
#          ),
#          pdk.Layer(
#              'ScatterplotLayer',
#              data=df,
#              get_position='[lon, lat]',
#              get_color='[200, 30, 0, 160]',
#              get_radius=200,
#          ),
#      ],
#  ))


if __name__ == "__main__":
    app()