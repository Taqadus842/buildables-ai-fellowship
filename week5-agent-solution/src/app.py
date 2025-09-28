"""
Streamlit demo app
- Upload text/pdf/docx, index (build) and ask questions
- For demo simplicity, uses the llama_index_agent query engine if available
"""
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Contract Quick-Summary", layout="wide")

st.title("Contract Quick-Summary — Demo")

st.sidebar.header("Actions")
action = st.sidebar.selectbox("Action", ["About", "Build Index", "Upload Document", "Ask Question", "Agent Tools"])

if action == "About":
    st.write("This demo summarizes contracts, flags risky clauses, and answers questions grounded in the uploaded documents.")
    st.write("Place sample documents in `/data/` then Build Index.")
    st.write("Make sure OPENAI_API_KEY is set in .env.")

if action == "Build Index":
    st.write("Building index from files in `/data/`...")
    import subprocess, sys
    try:
        res = subprocess.run([sys.executable, "src/llama_index_agent.py", "--build"], capture_output=True, text=True)
        st.text(res.stdout + "\n" + res.stderr)
        st.success("Index build attempted — check console output.")
    except Exception as e:
        st.error("Error running index build: " + str(e))

if action == "Upload Document":
    uploaded = st.file_uploader("Upload a contract (txt, pdf, docx)", type=["txt","pdf","docx"])
    if uploaded:
        save_path = os.path.join("data", uploaded.name)
        with open(save_path, "wb") as f:
            f.write(uploaded.getbuffer())
        st.success(f"Saved to {save_path}")

if action == "Ask Question":
    query = st.text_input("Ask a question about the uploaded contracts:", "")
    if st.button("Run Query"):
        if not query:
            st.warning("Please enter a question.")
        else:
            st.info("Querying index...")
            try:
                from src.llama_index_agent import query_index
                resp = query_index(query)
                st.write(resp)
            except Exception as e:
                st.error("Query failed. Ensure index is built and OPENAI_API_KEY is set. Error: " + str(e))

if action == "Agent Tools":
    st.write("LangChain agent tools demo (ClauseClassifier + Calculator).")
    clause = st.text_area("Paste a clause to classify (demo heuristic):", "The provider shall indemnify the client...")
    if st.button("Classify Clause"):
        try:
            from src.tools.custom_tool import ClauseClassifierTool
            t = ClauseClassifierTool()
            st.write(t._run(clause))
        except Exception as e:
            st.error("Tool error: " + str(e))
