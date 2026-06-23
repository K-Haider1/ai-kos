from services.vector_store import VectorStore

def test_vector_store():
    store = VectorStore()
    assert store is not None