import os
from typing import Union

# OpenAI
try:
    import openai
except ImportError:
    openai = None

# Hugging Face Inference
try:
    from transformers import pipeline
except ImportError:
    pipeline = None

# ------------------------
# OpenAI summarization
# ------------------------
def summarize_openai(text: str, model: str = "gpt-3.5-turbo") -> dict:
    if openai is None:
        return {"error": "openai library not installed"}
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return {"error": "OPENAI_API_KEY environment variable not set"}

    try:
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": f"Summarize the following text:\n{text}"}],
            max_tokens=150
        )
        summary = response.choices[0].message.content
        return {"summary": summary.strip()}
    except Exception as e:
        return {"error": str(e)}

# ------------------------
# Hugging Face summarization
# ------------------------
def summarize_hf_inference(text: str, repo_id: str = "google/flan-t5-small") -> dict:
    if pipeline is None:
        return {"error": "transformers library not installed"}

    try:
        summarizer = pipeline("summarization", model=repo_id)
        summary_list = summarizer(text, max_length=150, min_length=30, do_sample=False)
        summary_text = summary_list[0]["summary_text"]
        return {"summary": summary_text.strip()}
    except Exception as e:
        return {"error": str(e)}

# ------------------------
# Gemini placeholder
# ------------------------
def summarize_gemini_placeholder(text: str) -> dict:
    # Placeholder function until Gemini API is integrated
    try:
        summary = f"(Gemini placeholder) {text[:150]}..."  # Simple truncated summary
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}

