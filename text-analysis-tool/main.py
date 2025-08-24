import streamlit as st
from utils.llm_helpers import summarize_openai, summarize_hf_inference, summarize_gemini_placeholder
from utils.tokenizer_helpers import analyze_tokens
from langdetect import detect
from textstat import flesch_reading_ease

st.title("📝 Text Analysis Tool")

text_input = st.text_area("Enter text for analysis:", height=200)

if st.button("Run Analysis"):
    if text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        st.subheader("🔹 Summaries")
        st.write("**OpenAI**:", summarize_openai(text_input))
        st.write("**HuggingFace Mistral**:", summarize_hf_inference(text_input))
        st.write("**Gemini (placeholder)**:", summarize_gemini_placeholder(text_input))

        st.subheader("🔹 Tokenization")
        token_stats = analyze_tokens(text_input)
        st.json(token_stats)

        st.subheader("🔹 Language Detection")
        st.write("Detected Language:", detect(text_input))

        st.subheader("🔹 Readability")
        st.write("Flesch Reading Ease:", flesch_reading_ease(text_input))

