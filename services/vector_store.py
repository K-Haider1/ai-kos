"""
Vector Store Service
Author :
Kahkashan Haider
"""

import chromadb

class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="data/vector_store")
        self.collection = self.client.get_or_create_collection(name = "ai_kos_documents")

    def add_documents(self,
                      ids,
                      documents,
                      embeddings):
        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings.tolist()
        )
    
    def count(self):
        return self.collection.count()
    
if __name__ == "__main__":
    store = VectorStore()
    print(f"Document Count : {store.count()}")
    