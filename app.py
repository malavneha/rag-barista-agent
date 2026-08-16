import streamlit as st
from agent import search_menu

st.title("☕ RAG Barista Agent")

query = st.text_input("What coffee are you looking for?")

if query:
    result = search_menu(query)

    st.subheader("Recommendations")

    for item in result["results"]:
        st.write("☕", item["name"])
        st.write(item["description"])
