from embeddings.embedding_service import (
    EmbeddingService
)
def test_embedding_embeddings():
    service = EmbeddingService()
    embeddings = (
        service.generate_embeddings(
            ["AI KOS"]
        )
    )
    assert len(embeddings) == 1
    