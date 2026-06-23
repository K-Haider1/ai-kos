"""
Embedding Service

Author : 
Kahkashan Haider
"""

from sentence_transformers import SentenceTransformer
from embeddings.embedding_model import MODEL_NAME

class EmbeddingService:
    """
    Generate embeddings using BGE model.
    """

    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)
    
    def generate_embeddings(self, texts:list[str]):
        return self.model.encode(
            texts,
            convert_to_numpy = True
        )
    
if __name__ == "__main__":
    service = EmbeddingService()
    texts = [
        "Artificial Intelligence (AI) is transforming the way we interact with technology.",
        "Machine learning is a subset of AI that focuses on building systems that learn from data.",
        "Natural Language Processing (NLP) enables machines to understand and interpret human language."

    ]
    embeddings = service.generate_embeddings(texts)
    print(f"Generated Embeddings : {len(embeddings)}")
    print(f"Embedding Dimension : {len(embeddings[0])}")
    
