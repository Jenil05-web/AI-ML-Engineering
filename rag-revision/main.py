from src.ingestion.document_loader import load_pdf
from src.chunking.document_chuking import split_documents
from src.embeddings.document_embedding import generate_embeddings
from src.vectorstore.chromadb import create_vectorstore
from src.retrieval.document_retrieval import retrieve_documents
from dotenv import load_dotenv

load_dotenv()


docs = load_pdf(r"C:\Users\jenil\OneDrive\Desktop\Machine learning\rag-revision\data\sample.pdf")
chunks = split_documents(docs)
embeddings = generate_embeddings(chunks)
vector_store = create_vectorstore(chunks)
query = "List the Company policies "

print("\n Retrieved Results:")
print(f"Total pages loaded: {len(docs)}")

for i, chunk in enumerate(chunks):

    print(f"\nChunk {i+1}")
    print("Content:", chunk.page_content)
    print("Metadata:", chunk.metadata)
    print("Length:", len(chunk.page_content))
    print("First embedding:", embeddings[0])
    print(f"\nResult {i+1}:")
   