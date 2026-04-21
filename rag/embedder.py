from typing import List
import numpy as np
from sentence_transformers import SentenceTransformer

# Pick a small, fast model (you can change later)
DEFAULT_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

class Embedder:
    def __init__(self, model_name: str = DEFAULT_MODEL_NAME):
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts: List[str]) -> np.ndarray:
        """
        Embed a list of texts into a 2D numpy array of shape (n_texts, dim).
        """
        # convert_to_numpy=True returns np.ndarray directly
        embeddings = self.model.encode(
            texts,
            batch_size=32,
            show_progress_bar=True,
            convert_to_numpy=True,
        )
        return embeddings

    def embed_query(self, text: str) -> np.ndarray:
        """
        Embed a single query text into a 2D array of shape (1, dim).
        """
        emb = self.model.encode(
            [text],
            batch_size=1,
            show_progress_bar=False,
            convert_to_numpy=True,
        )
        return emb