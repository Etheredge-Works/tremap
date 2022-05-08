import streamlit as st
import data
import exploration
import m


df = data.get_data()
names = data.get_names()

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
        n = len(names) // 4
        selections = st.multiselect(
            f"Select species (\"{names[0]}\"    -    \"{names[n]}\"):", names[:n])
        selections += st.multiselect(
            f"Select species (\"{names[n+1]}\"    -    \"{names[n*2]}\"):", names[n+1:n*2])
        selections += st.multiselect(
            f"Select species (\"{names[(n*2)+1]}\"    -    \"{names[n*3]}\"):", names[(n*2)+1:n*3])
        selections += st.multiselect(
            f"Select species (\"{names[(n*3)+1]}\"    -    \"{names[n*4]}\"):", names[(n*3)+1:])
        # st.write("You selected:", selections)
        # selections = st.multiselect(
        #     "Select species:", 
        #     data.df, 
        #     format_func=lambda x: x['scientificName']
        # )

        images, captions, name, final = data.get_images(selections)
        # print(images)
        # print(captions)
        # print(name)
        # print(final)
        st.write("# Pressings")
        st.image(images, caption=final)

        # if mode_select == "Advanced":
        #     exploration.app()

        st.write("# Map")
        # elif mode_select == "Map":
        m.app(selections)
