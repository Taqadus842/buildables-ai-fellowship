import os
import docx2txt
from PyPDF2 import PdfReader

def load_documents(folder="data"):
    texts = []
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                texts.append(f.read())
        elif file.endswith(".docx"):
            texts.append(docx2txt.process(path))
        elif file.endswith(".pdf"):
            reader = PdfReader(path)
            texts.append("\n".join([page.extract_text() for page in reader.pages]))
    return texts
