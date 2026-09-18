from rag.loader import load_documents

documents = load_documents()

print(f"Loaded{len(documents)} documents:   ")

for doc in documents[:2]:
    print("--Document--")

    print(doc.page_content[:500])
    print(doc.metadata)
