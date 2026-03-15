import fitz
from pathlib import Path


def extract_text_from_pdf(pdf_path: str) -> list:
    """Extract text page-by-page with metadata."""
    doc = fitz.open(pdf_path)
    pages = []
    paper_title = Path(pdf_path).stem

    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text").strip()
        if text and len(text) > 10:
            pages.append({
                "text": text,
                "page": page_num,
                "source": paper_title,
                "file_path": str(pdf_path)
            })

    doc.close()

    if not pages:
        print(f"[pdf_parser] WARNING: No text extracted from '{paper_title}'.")
        print(f"[pdf_parser] This PDF may be scanned. Please use text-based PDFs.")

    return pages
