from logging import PlaceHolder
import streamlit as st
import py_data
import exploration
import m
from itertools import cycle


df = py_data.get_data()
print("got data")
# names = data.get_names()

@st.cache
def get_values(key):
    global df
    return df[key].unique()


if __name__ == "__main__":
    # with st.sidebar:
        # with st.echo():
            # st.write("Modes")
        # st.title("Modes")
    mode_select = st.sidebar.radio(
        "Select mode",
        ["Basic", "Advanced"]
    )

    st.image("tremap_logos/tremap-green.png")
    print("got image")

    st.write("NOTE: Pressing images will NOT load on Google Chrome due to being hosted through HTTP.")
    st.write("Please be patient with loading. There's a lot of records :)")
    print("got heading")

    # st.write(df.columns)

    # selections = st.multiselect(
    if mode_select == "Basic":
        key = 'stateProvince'
        c = df[df['countryCode'] == 'US']

        selections = st.multiselect(f"Select state...", sorted(c[key].unique())) 

        images, captions, name, final, raw_df = py_data.get_images(key, selections)

        st.write("# Map")
        m.app(key, selections) 
        print("got map")
        st.write("# Pressings")
        st.write("NOTE: Pressing images will NOT load on Google Chrome due to being hosted through HTTP.")

        # with st.expander("See images"):
        if len(images) > 0:
            page_idx = st.selectbox("Page: ", list(range(1, len(images)//16)))
            start = (page_idx-1) * 16
            end = start + 16
            im_placeholder = st.empty()
            with im_placeholder.container():
                # cols = cycle(st.columns(4))
                cols = cycle(im_placeholder.columns(4))
                for col, image, caption in zip(cols, images[start:end], captions[start:end]):
                    # im_placeholder.image(image, caption)
                    col.image(image, width=150, caption=caption)

    elif mode_select == "Advanced":

        #key = st.radio("Select key", df.columns, index=11)
        # key = "scientificName"
        keys = ["scientificName", "countryCode", "stateProvince", "species", "taxonKey", "speciesKey", "kingdom",
                    "genus", "taxonRank", "decimalLatitute", "decimalLongitude"]
        key = st.radio("Select key", keys, index=0)

        names = get_values(key)
        # if key in ["scientificName", "verbatimScientificName"]:
        # if False:
        #     n = len(names) // 4
        #     selections = st.multiselect(
        #         f"Select {key} (\"{names[0]}\"    -    \"{names[n]}\"):", names[:n])
        #     selections += st.multiselect(
        #         f"Select {key} (\"{names[n+1]}\"    -    \"{names[n*2]}\"):", names[n+1:n*2])
        #     selections += st.multiselect(
        #         f"Select {key} (\"{names[(n*2)+1]}\"    -    \"{names[n*3]}\"):", names[(n*2)+1:n*3])
        #     selections += st.multiselect(
        #         f"Select {key} (\"{names[(n*3)+1]}\"    -    \"{names[n*4]}\"):", names[(n*3)+1:])
        # else:
        selections = st.multiselect(
            f"Select {key}", names)
        # st.write("You selected:", selections)
        # selections = st.multiselect(
        #     "Select species:", 
        #     data.df, 
        #     format_func=lambda x: x['scientificName']
        # )
        st.write("# Map")
        # elif mode_select == "Map":
        m.app(key, selections)

        images, captions, name, final, raw_df = py_data.get_images(key, selections)
        # print(images)
        # print(captions)
        # print(name)
        # print(final)
        st.write("# Pressings")
        if len(images) > 0:
            page_idx = st.selectbox("Page: ", list(range(1, len(images)//16)))
            start = (page_idx-1) * 16
            end = start + 16
            im_placeholder = st.empty()
            with im_placeholder.container():
                # cols = cycle(st.columns(4))
                cols = cycle(im_placeholder.columns(4))
                for col, image, caption in zip(cols, images[start:end], captions[start:end]):
                    # im_placeholder.image(image, caption)
                    col.image(image, width=150, caption=caption)

        # if mode_select == "Advanced":
        #     exploration.app()

        with st.expander("All data"):
            st.write(raw_df)

