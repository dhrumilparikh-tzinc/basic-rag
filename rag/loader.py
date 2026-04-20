from pathlib import Path
from typing import List
import pandas as pd

DATA_DIR = Path("data")
CSV_PATH = DATA_DIR / "medquad.csv"  # update to real filename

# Update these constants after you inspect columns
QUESTION_COL = "question"   # e.g. "question" or "Question"
ANSWER_COL = "answer"       # e.g. "answer" or "Answer"
CATEGORY_COL = None         # e.g. "category" or disease if exists (optional)

def load_documents() -> List[str]:
    df = pd.read_csv(CSV_PATH)

    # Drop rows where question or answer is missing
    df = df.dropna(subset=[QUESTION_COL, ANSWER_COL])

    documents: List[str] = []

    for _, row in df.iterrows():
        q = str(row[QUESTION_COL]).strip()
        a = str(row[ANSWER_COL]).strip()

        parts = []
        if CATEGORY_COL is not None and CATEGORY_COL in df.columns:
            cat = str(row[CATEGORY_COL]).strip()
            parts.append(f"Category: {cat}")

        parts.append(f"Question: {q}")
        parts.append(f"Answer: {a}")

        text = "\n".join(parts)
        documents.append(text)

    return documents

if __name__ == "__main__":
    docs = load_documents()
    print("Loaded", len(docs), "documents")
    print("Example document:\n", docs[0])
    