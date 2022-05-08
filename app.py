import streamlit as st
import exploration
import m



with st.sidebar:
    # with st.echo():
    #     st.write("Modes")
    st.title("Modes")
mode_select = st.sidebar.radio(
    "Select mode",
    ["Basic", "Map", "Advanced"]
)

if mode_select == "Advanced":
    exploration.app()

elif mode_select == "Basic":
    pass

elif mode_select == "Map":
    m.app()
