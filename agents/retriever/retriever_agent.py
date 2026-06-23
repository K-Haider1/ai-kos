"""

Retriever Agent
Author : Kahkashan Haider
"""
from embeddings.embedding_service import EmbeddingService
from services.vector_store import VectorStore


class RetrieverAgent:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()

    def retrieve(self, query, top_k=3):

        query_embedding = (
            self.embedding_service.generate_embeddings(
                [query]
            )[0]
        )

        results = self.vector_store.query(
            query_embedding,
            top_k
        )

        return results