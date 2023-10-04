from pypdf import PdfReader

def readPattern(path):
    reader = PdfReader(path)

    title = reader.metadata.get("/Title")
    author = reader.metadata.get("/Author")

    patternInfo = {
        "title": title,
        "author": author
    }

    return reader.read(path)
    