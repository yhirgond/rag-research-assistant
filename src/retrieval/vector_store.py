import faiss
import numpy as np
import pickle
from pathlib import Path


class VectorStore:
    def __init__(self, dim: int = None):
        self.dim = dim
        self.index = faiss.IndexFlatIP(dim) if dim is not None else None
        self.metadata = []

    def add(self, embeddings: np.ndarray, chunks: list):
        if embeddings.ndim == 1:
            embeddings = embeddings.reshape(1, -1)
        if embeddings.shape[0] == 0:
            print("No embeddings to add!")
            return

        actual_dim = embeddings.shape[1]
        if self.index is None:
            self.dim = actual_dim
            self.index = faiss.IndexFlatIP(actual_dim)

        if actual_dim != self.dim:
            raise ValueError(
                f"Dimension mismatch: index={self.dim}, got={actual_dim}. "
                f"Delete saved index and re-index."
            )

        self.index.add(embeddings.astype("float32"))
        self.metadata.extend(chunks)
        print(f"Added {len(chunks)} chunks. Total: {self.index.ntotal}")

    def search(self, query_embedding: np.ndarray, top_k: int = 5) -> list:
        if query_embedding.ndim == 1:
            query_embedding = query_embedding.reshape(1, -1)
        scores, indices = self.index.search(
            query_embedding.astype("float32"), top_k
        )
        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx != -1:
                result = self.metadata[idx].copy()
                result["score"] = float(score)
                results.append(result)
        return results

    def save(self, path: str):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        faiss.write_index(self.index, f"{path}.faiss")
        with open(f"{path}.pkl", "wb") as f:
            pickle.dump(self.metadata, f)

    def load(self, path: str):
        self.index = faiss.read_index(f"{path}.faiss")
        self.dim = self.index.d
        with open(f"{path}.pkl", "rb") as f:
            self.metadata = pickle.load(f)

    def is_empty(self) -> bool:
        return self.index is None or self.index.ntotal == 0
