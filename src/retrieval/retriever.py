from src.embeddings.embedder import Embedder
from src.retrieval.vector_store import VectorStore


class Retriever:
    def __init__(self, embedder: Embedder, store: VectorStore):
        self.embedder = embedder
        self.store = store

    def retrieve(self, query: str, top_k: int = 5) -> list:
        query_embedding = self.embedder.embed_query(query)
        results = self.store.search(query_embedding, top_k=top_k)
        return results
