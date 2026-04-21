from pathlib import Path
from typing import List, Dict, Any

import numpy as np

from rag.loader import load_documents
from rag.chunker import chunk_documents
from rag.embedder import Embedder
from rag.faiss_store import (
    build_faiss_index,
    save_faiss_index,
    save_metadata,
    FAISS_DIR,
)


def main():
    print("Loading documents...")
    documents = load_documents()
    print(f"Loaded {len(documents)} documents")

    print("Chunking documents...")
    chunks: List[str] = chunk_documents(documents, chunk_size=500, overlap=100)
    print(f"Total chunks: {len(chunks)}")

    # Build metadata: at least store text; later you can add doc_id, etc.
    metadata: List[Dict[str, Any]] = []
    for idx, chunk_text in enumerate(chunks):
        # doc_id could come from loader; for now we store only chunk index + text
        metadata.append(
            {
                "chunk_id": idx,
                "text": chunk_text,
                # "doc_id": ...  # you can add later
            }
        )

    print("Embedding chunks...")
    embedder = Embedder()
    embeddings = embedder.embed_texts(chunks)  # shape (n_chunks, dim)
    print(f"Embeddings shape: {embeddings.shape}")

    print("Building FAISS index...")
    index = build_faiss_index(embeddings)

    print("Saving index and metadata...")
    FAISS_DIR.mkdir(exist_ok=True)
    save_faiss_index(index)
    save_metadata(metadata)

    print("Done. Index and metadata saved in", FAISS_DIR)


if __name__ == "__main__":
    main()