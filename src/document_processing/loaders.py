from pypdf import PdfReader
from pathlib import Path
from docx import Document

def load_multiple_files(file_input):
    results = ""
    for file in file_input:
        results += loadfile(file) + "\n"
    return results
    
def loadfile(file_input):

    if hasattr(file_input, 'read'):
        file_name = file_input.name
        ext = Path(file_name).suffix.lower()
        if ext == ".pdf":
            reader = PdfReader(file_input)
            pages = [page.extract_text() for page in reader.pages]
            pages = [p for p in pages if p is not None]
            return "\n".join(pages)
        elif ext == ".txt":
            return file_input.read().decode("utf-8")
        elif ext in [".doc", ".docx"]:
            doc = Document(file_input)
            return "\n".join([paragraph.text for paragraph in doc.paragraphs if paragraph.text is not None])
        else:
            raise ValueError(f"Unsupported file type: {ext}")
    else:
        try:
            ext = Path(file_input).suffix.lower()
            if ext == ".pdf":
                reader = PdfReader(file_input)
                pages = [page.extract_text() for page in reader.pages]
                pages = [p for p in pages if p is not None] 
                return "\n".join(pages)
            elif ext == ".txt":
                with open(file_input, "r") as f:
                    return f.read()
            elif ext in [".doc", ".docx"]:
                doc = Document(file_input)
                return "\n".join([paragraph.text for paragraph in doc.paragraphs if paragraph.text is not None])
            else:
                raise ValueError(f"Unsupported file type: {ext}")
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_input}")