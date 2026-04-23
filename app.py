from rag.generator import generate_answer
from db.logger import log_interaction

def main():
    print("Medical RAG Assistant (type 'quit' to exit)")
    while True:
        question = input("\nYour question: ").strip()
        if not question or question.lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            break

        print("\nThinking...\n")
        result = generate_answer(question, k=5)

        # Print answer
        print("Answer:")
        print(result["answer"])

        # Show retrieved chunks for debugging
        print("\n[Retrieved context snippets]")
        for i, ch in enumerate(result["chunks"], start=1):
            print(f"\n--- Chunk {i} (distance={ch['distance']:.4f}) ---")
            print(ch["text"][:400])

        # Log into PostgreSQL
        log_interaction(
            question=result["question"],
            answer=result["answer"],
            chunks=result["chunks"],
        )

if __name__ == "__main__":
    main()