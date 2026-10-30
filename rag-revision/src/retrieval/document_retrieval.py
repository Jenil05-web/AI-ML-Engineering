from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

def retrieve_documents(query):
    embedding_model = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vector_store = Chroma(
        collection_name="rag_collection",
        persist_directory="./chroma_db",
        embedding_function=embedding_model

    )

    results = vector_store.similarity_search(
        query,
        k=3
    )

    return results