from sentence_transformers import CrossEncoder

def rerank_documents(query,documents):
    reranker = CrossEncoder(
        "BAAI/bge-reranker-base"
    )

    pairs = [
        [query, __doc__.page_content]
        for __doc__ in documents
    ]
    scores =reranker.predict(pairs)

    ranked_documents = sorted(
        zip(documents, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked_documents