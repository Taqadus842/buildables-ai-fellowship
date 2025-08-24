import tiktoken
from transformers import AutoTokenizer

def analyze_gpt_tokens(text: str, model: str = "gpt-3.5-turbo"):
    """
    Analyze tokens using OpenAI GPT tokenizer (tiktoken).
    Returns tokenized text and token count.
    """
    try:
        enc = tiktoken.encoding_for_model(model)
    except KeyError:
        enc = tiktoken.get_encoding("cl100k_base")  # fallback

    tokens = enc.encode(text)
    return {
        "tokens": tokens,
        "num_tokens": len(tokens)
    }

def analyze_hf_tokenizer(text: str, model_name: str = "gpt2"):
    """
    Analyze tokens using Hugging Face tokenizer.
    Returns tokenized text and token count.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokens = tokenizer.encode(text)
    return {
        "tokens": tokens,
        "num_tokens": len(tokens)
    }

