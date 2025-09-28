import streamlit as st
from llama_index_agent import build_index, query_index
from agent import run_agent

st.set_page_config(page_title="Contract Analyzer Assistant", layout="wide")

st.title("📑 Contract Analyzer Assistant")

st.sidebar.header("Controls")
choice = st.sidebar.selectbox("Choose Action", ["Build Index", "Query Contract", "Run Agent Tool"])

if choice == "Build Index":
    if st.button("Build Index from /data"):
        build_index()
        st.success("Index built successfully!")

elif choice == "Query Contract":
    query = st.text_input("Enter your query:")
    if st.button("Ask"):
        if query:
            response = query_index(query)
            st.write("### Answer")
            st.write(response)

elif choice == "Run Agent Tool":
    query = st.text_input("Enter your agent query (e.g., calculate penalties):")
    if st.button("Run"):
        if query:
            answer = run_agent(query)
            st.write("### Agent Response")
            st.write(answer)
