from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

def extract_pdf_text(pdf_path: str) -> str:
    """
    Extract text from a PDF file.
    """
    pdfreader = PdfReader(pdf_path)
    raw_text = ''
    for page in pdfreader.pages:
        content = page.extract_text()
        if content:
            raw_text += content
    return raw_text

def split_text(raw_text: str, chunk_size: int = 800, chunk_overlap: int = 200) -> list:
    """
    Split extracted text into chunks.
    """
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=chunk_size, 
        chunk_overlap=chunk_overlap,
        length_function=len,
    )
    texts = text_splitter.split_text(raw_text)
    return texts
