from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os
# import openai
from dotenv import load_dotenv


load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

def create_vector_store(texts: list) -> FAISS:
    """
    Create a vector store using OpenAI embeddings.
    """
    embeddings = OpenAIEmbeddings(openai_api_key=openai_key)
    
    document_search = FAISS.from_texts(texts, embeddings)
    return document_search
