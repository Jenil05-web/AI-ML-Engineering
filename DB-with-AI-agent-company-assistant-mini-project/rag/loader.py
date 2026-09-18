from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

def load_documents():
    documents = []
    pdf_folder = Path("data/documents")

    for pdf_file in pdf_folder.glob("*.pdf"):
        loader = PyPDFLoader(str(pdf_file))
        documents.extend(loader.load())

    return documents