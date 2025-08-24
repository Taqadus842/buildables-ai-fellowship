import google.generativeai as genai
from openai import OpenAI
from mistralai import Mistral

from config import OPENAI_API_KEY, GOOGLE_API_KEY, MISTRAL_API_KEY

# Setup clients
genai.configure(api_key=GOOGLE_API_KEY)
openai_client = OpenAI(api_key=OPENAI_API_KEY)
mistral_client = Mistral(api_key=MISTRAL_API_KEY)

def summarize_gemini(text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"Summarize:\n{text}")
    return response.text

def summarize_chatgpt(text):
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Summarize:\n{text}"}]
    )
    return response.choices[0].message.content

def summarize_mistral(text):
    response = mistral_client.chat.complete(
        model="mistral-tiny",
        messages=[{"role": "user", "content": f"Summarize:\n{text}"}]
    )
    return response.choices[0].message["content"]
