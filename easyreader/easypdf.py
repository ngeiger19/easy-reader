from pypdf import PdfReader

def readPattern(path):
    pdf_reader = PdfReader(path)
    return len(pdf_reader.pages)
    