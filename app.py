import streamlit as st
import data
import exploration
import m
from itertools import cycle


df = data.get_data()
# names = data.get_names()

if __name__ == "__main__":
    with st.sidebar:
        # with st.echo():
        #     st.write("Modes")
        st.title("Modes")
    mode_select = st.sidebar.radio(
        "Select mode",
        ["Basic", "Advanced"]
    )


    # st.write(df.columns)

    # selections = st.multiselect(
    if mode_select == "Basic":
        pass   
    elif mode_select == "Advanced":

        key = st.radio("Select key", df.columns, index=1)
        # key = "scientificName"

        names = sorted(df[key].unique())
        # if key in ["scientificName", "verbatimScientificName"]:
        if False:
            n = len(names) // 4
            selections = st.multiselect(
                f"Select {key} (\"{names[0]}\"    -    \"{names[n]}\"):", names[:n])
            selections += st.multiselect(
                f"Select {key} (\"{names[n+1]}\"    -    \"{names[n*2]}\"):", names[n+1:n*2])
            selections += st.multiselect(
                f"Select {key} (\"{names[(n*2)+1]}\"    -    \"{names[n*3]}\"):", names[(n*2)+1:n*3])
            selections += st.multiselect(
                f"Select {key} (\"{names[(n*3)+1]}\"    -    \"{names[n*4]}\"):", names[(n*3)+1:])
        else:
            selections = st.multiselect(
                f"Select {key}", sorted(df[key].unique()))
        # st.write("You selected:", selections)
        # selections = st.multiselect(
        #     "Select species:", 
        #     data.df, 
        #     format_func=lambda x: x['scientificName']
        # )

        images, captions, name, final, raw_df = data.get_images(key, selections)
        # print(images)
        # print(captions)
        # print(name)
        # print(final)
        st.write("# Pressings")
        with st.expander("See images"):
            cols = cycle(st.columns(4))
            for idx, image in enumerate(images):
                next(cols).image(image, width = 150, caption=final[idx])

        st.write("# All data")
        st.write(raw_df)
        # if mode_select == "Advanced":
        #     exploration.app()

        st.write("# Map")
        # elif mode_select == "Map":
        m.app(key, selections)
