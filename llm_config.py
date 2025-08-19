import os
from langchain.chat_models import ChatOpenAI

def get_llm():
    return ChatOpenAI(
        temperature=0.2,
        model_name="gpt-4",
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
