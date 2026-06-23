"""
Document Ingestion Pipeline
Author :
Kahkashan Haider
"""

import uuid

from ingestion.pdf_loader import load_text_file
from ingestion.text_cleaner import clean_text
from ingestion.chunker import chunk_text

from embeddings.embedding_service import EmbeddingService
from services.vector_store import VectorStore

def ingest_document(file_path:str):
    print("Loading document...")
    text = load_text_file(file_path)
    print("Cleaning Document...")
    cleaned_text = clean_text(text)
    print("Chunking Document...")
    chunks = chunk_text(
        cleaned_text,
        chunk_size=100,
        chunk_overlap=20
        )
    print(f"Chunks Generated : {len(chunks)}")
    embedding_service = EmbeddingService()
    embeddings = (
        embedding_service.generate_embeddings(
            chunks
        )
    )

    vector_store = VectorStore()
    ids = [
        str(uuid.uuid4())
        for _ in chunks
    ]
    vector_store.add_documents(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )
    print(f"Stored {len(chunks)} Chunks Successfully in Vector Store.")

if __name__ == "__main__":
    ingest_document("data/raw/sample_document.txt")
        

    