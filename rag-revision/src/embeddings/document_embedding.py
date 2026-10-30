from langchain_openai import OpenAIEmbeddings

def generate_embeddings(chunks):
    embedding_model = OpenAIEmbeddings(
        model = "text-embedding-3-small"
    )

    texts = [chunk.page_content for chunk in chunks]
    embeddings = embedding_model.embed_documents(texts)
    return embeddings