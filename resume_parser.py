import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def extract_cgpa(text):
    match = re.search(r'CGPA[:\s]*([0-9]\.?[0-9]*)', text, re.IGNORECASE)
    if match:
        return float(match.group(1))
    return 0.0
