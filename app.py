import streamlit as st
import data
import exploration
import m



if __name__ == "__main__":
    with st.sidebar:
        # with st.echo():
        #     st.write("Modes")
        st.title("Modes")
    mode_select = st.sidebar.radio(
        "Select mode",
        ["Basic", "Map", "Advanced"]
    )

    st.write(data.df.columns)
    selections = st.multiselect("Select species:", data.df['scientificName'].to_list())

    if mode_select == "Advanced":
        exploration.app()

    elif mode_select == "Basic":
        pass

    # elif mode_select == "Map":
    m.app(selections)
