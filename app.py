import streamlit as st
import data
import exploration
import m


df = data.get_data()

if __name__ == "__main__":
    with st.sidebar:
        # with st.echo():
        #     st.write("Modes")
        st.title("Modes")
    mode_select = st.sidebar.radio(
        "Select mode",
        ["Basic", "Map", "Advanced"]
    )


    st.write(df.columns)

    selections = st.multiselect(
        "Select species:", data.get_names())
    # selections = st.multiselect(
    #     "Select species:", 
    #     data.df, 
    #     format_func=lambda x: x['scientificName']
    # )

    if mode_select == "Advanced":
        exploration.app()

    elif mode_select == "Basic":
        pass

    # elif mode_select == "Map":
    m.app(selections)
