import re

POS_WORDS = {"good","great","happy","love","excellent","positive","improve","benefit","success"}
NEG_WORDS = {"bad","sad","terrible","hate","worse","negative","problem","fail","loss"}

def sentiment_simple(text):
    """Very small word-list sentiment scorer. Returns label and score (pos-neg)."""
    words = [re.sub(r'[^a-zA-Z]', '', w).lower() for w in text.split()]
    score = sum(1 for w in words if w in POS_WORDS) - sum(1 for w in words if w in NEG_WORDS)
    label = "neutral"
    if score > 0:
        label = "positive"
    elif score < 0:
        label = "negative"
    return {"label": label, "score": score}

def text_statistics(text):
    import re
    words = re.findall(r'\b\w+\b', text)
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]
    avg_word_length = sum(len(w) for w in words) / len(words) if words else 0
    return {
        "word_count": len(words),
        "sentence_count": len(sentences),
        "avg_word_length": round(avg_word_length, 2),
        "unique_words": len(set(words))
    }

