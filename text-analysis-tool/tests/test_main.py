from utils.llm_helpers import summarize_gemini_placeholder
from utils.tokenizer_helpers import analyze_tokens

def test_placeholder_summary():
    text = "This is a test sentence for Gemini summarizer."
    result = summarize_gemini_placeholder(text)
    assert "Gemini summary" in result

def test_tokenizer():
    text = "Hello world"
    result = analyze_tokens(text)
    assert result["num_tokens"] > 0

