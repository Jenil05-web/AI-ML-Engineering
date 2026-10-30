from langchain_classic.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

def create_hybrid_retriever(chunks):
    
    embedding_model = OpenAIEmbeddings(
        model = "text-embedding-3-small"
    )
# Semantic Retriever
    vector_store = Chroma(
        collection_name="rag_collection",
        persist_directory="./chroma_db",
        embedding_function=embedding_model
    )

    semantic_retriever = vector_store.as_retriever(
        search_kwargs={"k":4}

    )

    # KeyWord Retriever

    keyword_retriever = BM25Retriever.from_documents(chunks)
    keyword_retriever.k = 4

    # Combining both retrievers : 
    hybrid_retriever = EnsembleRetriever(
        retrievers=[
            semantic_retriever,
            keyword_retriever
        ],
        weights = [0.5,0.5]
    )

    return hybrid_retriever





