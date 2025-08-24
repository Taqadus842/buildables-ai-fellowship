import streamlit as st
import json
from utils.llm_helpers import summarize_openai, summarize_hf_inference, summarize_gemini_placeholder
from utils.tokenizer_helpers import analyze_gpt_tokens, analyze_hf_tokenizer
from utils.analysis import sentiment_simple, text_statistics
from config import COST_PER_1K_TOKENS_USD

st.set_page_config(page_title="Text Analysis Tool", layout="centered")
st.title("📝 Text Analysis Tool")

# Input text
text = st.text_area("Paste your text here", height=300)

col1, col2 = st.columns(2)

with col1:
    model_choice = st.selectbox("OpenAI model (for summary)", ["gpt-3.5-turbo", "gpt-4o-mini"])
    do_openai = st.checkbox("Use OpenAI (ChatGPT)", value=True)

with col2:
    hf_repo = st.text_input("HuggingFace repo (for HF summary)", "google/flan-t5-small")
    do_hf = st.checkbox("Use HuggingFace Inference", value=False)

if st.button("Analyze") and text.strip():
    st.subheader("Tokenization")
    gpt_tok = analyze_gpt_tokens(text)
    hf_tok = analyze_hf_tokenizer(text)
    st.write("GPT-style token count:", gpt_tok.get("num_tokens", 0))
    st.write("HuggingFace (BERT) token count:", hf_tok.get("num_tokens", 0))
    st.write("---")

    results = {"text": text, "tokens": {"gpt": gpt_tok, "hf": hf_tok}}

    # Summaries
    st.subheader("Summaries")

    # OpenAI
    if do_openai:
        with st.spinner("Calling OpenAI..."):
            r = summarize_openai(text, model=model_choice)
            if isinstance(r, dict) and "error" in r:
                st.error("❌ OpenAI error: " + r["error"])
            else:
                st.success("✅ OpenAI summary")
                st.write(r.get("summary") if isinstance(r, dict) else r)
                results["openai"] = r

    # Hugging Face
    if do_hf:
        with st.spinner("Calling HuggingFace Inference..."):
            r = summarize_hf_inference(text, repo_id=hf_repo)
            if isinstance(r, dict) and "error" in r:
                st.error("❌ Hugging Face error: " + r["error"])
            else:
                st.success("✅ HuggingFace summary")
                st.write(r.get("summary") if isinstance(r, dict) else r)
                results["huggingface"] = r

    # Gemini placeholder
    st.markdown("**Gemini Summary (Placeholder)**")
    gem = summarize_gemini_placeholder(text)
    if isinstance(gem, dict) and "error" in gem:
        st.info("Gemini: " + gem["error"])
    else:
        st.write(gem.get("summary") if isinstance(gem, dict) else gem)
        results["gemini"] = gem

    # Cost estimate
    est_cost_usd = None
    if "num_tokens" in gpt_tok:
        est_cost_usd = (gpt_tok["num_tokens"] / 1000.0) * COST_PER_1K_TOKENS_USD
    st.subheader("Cost estimate (basic)")
    st.write(f"Estimated cost (USD) for OpenAI-like tokens: {est_cost_usd}")

    # Sentiment
    st.subheader("Sentiment (simple)")
    sent = sentiment_simple(text)
    st.json(sent)
    results["sentiment"] = sent

    # Text statistics
    st.subheader("Text statistics")
    stats = text_statistics(text)
    st.json(stats)
    results["statistics"] = stats

    # Export JSON
    st.download_button(
        "Download JSON results",
        data=json.dumps(results, indent=2),
        file_name="analysis_results.json",
        mime="application/json"
    )
else:
    st.info("Paste some text and press Analyze.")

