import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf_document:
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text += page.get_text()
            print(page_num + 1)
        # page = pdf_document.load_page(54)
        # text = page.get_text()
    return text
