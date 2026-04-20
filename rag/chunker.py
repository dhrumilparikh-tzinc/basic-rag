from typing import List

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> List[str]:
    """
    Splits a long string into overlapping chunks by characters.
    """
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        # Move the window with overlap
        start = end - overlap
        if start < 0:
            start = 0
    return chunks

def chunk_documents(
    documents: List[str],
    chunk_size: int = 500,
    overlap: int = 100
) -> List[str]:
    all_chunks: List[str] = []
    for doc_id, doc in enumerate(documents):
        doc_chunks = chunk_text(doc, chunk_size=chunk_size, overlap=overlap)
        all_chunks.extend(doc_chunks)
    return all_chunks

if __name__ == "__main__":
    # Quick self‑test
    sample = "This is a sample long text. " * 50
    cs = chunk_text(sample, chunk_size=100, overlap=20)
    print("Chunks:", len(cs))
    print(cs[0])