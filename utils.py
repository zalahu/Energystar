from langchain_community.document_loaders import PyPDFLoader, UnstructuredWordDocumentLoader, UnstructuredFileLoader
import os
import tempfile

def load_documents(uploaded_files):
    all_docs = []
    for file in uploaded_files:
        ext = os.path.splitext(file.name)[1].lower()
        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
            tmp.write(file.read())
            tmp_path = tmp.name
        if ext == ".pdf":
            loader = PyPDFLoader(tmp_path)
        elif ext in [".docx", ".doc"]:
            loader = UnstructuredWordDocumentLoader(tmp_path)
        else:
            loader = UnstructuredFileLoader(tmp_path)
        all_docs.extend(loader.load())
    return all_docs
