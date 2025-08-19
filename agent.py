from langchain.chains import RetrievalQA
from llm_config import get_llm
from vector_store import create_vector_store

def build_agent(documents):
    vectorstore = create_vector_store(documents)
    retriever = vectorstore.as_retriever()
    llm = get_llm()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain
