"""
ingest.py
- Utility to load different file types into plain text for indexing.
- Supports .txt, .pdf, .docx
"""
import os
from typing import List
import pdfplumber
import docx

def read_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def read_pdf(path):
    text = []
    with pdfplumber.open(path) as pdf:
        for p in pdf.pages:
            text.append(p.extract_text() or "")
    return "\n".join(text)

def read_docx(path):
    doc = docx.Document(path)
    return "\n".join([p.text for p in doc.paragraphs])

def load_documents_from_dir(data_dir="data"):
    docs = []
    for fn in os.listdir(data_dir):
        path = os.path.join(data_dir, fn)
        if fn.lower().endswith(".txt"):
            docs.append({"filename": fn, "text": read_txt(path)})
        elif fn.lower().endswith(".pdf"):
            docs.append({"filename": fn, "text": read_pdf(path)})
        elif fn.lower().endswith(".docx"):
            docs.append({"filename": fn, "text": read_docx(path)})
    return docs

if __name__ == "__main__":
    docs = load_documents_from_dir()
    print(f"Loaded {len(docs)} documents.")
