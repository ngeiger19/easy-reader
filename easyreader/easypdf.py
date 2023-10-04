from pypdf import PdfReader

def readPattern(path):
    reader = PdfReader(path)

    title = reader.metadata.get("/Title")
    author = reader.metadata.get("/Author")

    content = ""
    
    for page in reader.pages:
        content += page.extract_text()

    patternInfo = {
        "title": title,
        "author": author,
        "content": content
    }

    return patternInfo

