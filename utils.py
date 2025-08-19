from langchain.document_loaders import PyPDFLoader, UnstructuredWordDocumentLoader, UnstructuredFileLoader
import os

def load_documents(uploaded_files):
    all_docs = []
    for file in uploaded_files:
        ext = os.path.splitext(file.name)[1].lower()
        if ext == ".pdf":
            loader = PyPDFLoader(file)
        elif ext in [".docx", ".doc"]:
            loader = UnstructuredWordDocumentLoader(file)
        else:
            loader = UnstructuredFileLoader(file)
        all_docs.extend(loader.load())
    return all_docs
