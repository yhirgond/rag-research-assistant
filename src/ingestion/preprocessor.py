import re


def clean_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('\x00', '')
    return text.strip()


def preprocess_pages(pages: list) -> list:
    cleaned = []
    for page in pages:
        cleaned_text = clean_text(page["text"])
        if len(cleaned_text) > 10:
            page["text"] = cleaned_text
            cleaned.append(page)
    return cleaned
