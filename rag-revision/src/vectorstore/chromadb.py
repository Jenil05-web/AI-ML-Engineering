from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

def create_vectorstore(chunks):
    embedding_model = OpenAIEmbeddings(
        model = "text-embedding-3-small"
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding = embedding_model,
        collection_name = "rag_collection",
        persist_directory="./chroma_db"
    )
    return vectorstore