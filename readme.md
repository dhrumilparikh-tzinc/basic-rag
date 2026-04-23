# Basic Medical RAG

A Retrieval Augmented Generation assignment project using the MedQuAD dataset, SentenceTransformers embeddings, FAISS retrieval, Google Gemini generation, and PostgreSQL logging.

## What This Project Includes

- CSV loading and preprocessing for MedQuAD
- Character-based chunking with metadata preservation
- Embedding generation with `sentence-transformers/all-MiniLM-L6-v2`
- FAISS index build, save, and reload support
- Retrieval of top-k relevant chunks
- Gemini answer generation grounded in retrieved context
- PostgreSQL logging for each Q&A interaction

## Project Structure

```text
basic_rag_assignment/
|-- app.py
|-- config.py
|-- requirements.txt
|-- readme.md
|-- .env
|-- .env.example
|-- data/
|   |-- medquad.csv
|-- db/
|   |-- __init__.py
|   |-- db.py
|   |-- logger.py
|   |-- models.py
|-- faiss_index/
|   |-- index.faiss
|   |-- index.pkl
|-- rag/
|   |-- __init__.py
|   |-- chunker.py
|   |-- embedder.py
|   |-- faiss_store.py
|   |-- generator.py
|   |-- loader.py
|   |-- models.py
|   |-- retriever.py
|-- scripts/
|   |-- __init__.py
|   |-- build_index.py
|   |-- download_kaggle_data.py
|   |-- init_db.py
|   |-- inspect_medquad.py
|   |-- test_medquad_preprocessing.py
```

## Setup

### 1. Create and activate the virtual environment

```powershell
cd C:\Users\Dhrumil.parikh\basic_rag_assignment
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Create `.env`

Copy `.env.example` to `.env` and replace the placeholder values with your real credentials.

Expected variables:

```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.0-flash
KAGGLE_USERNAME=your_kaggle_username
KAGGLE_KEY=your_kaggle_api_key
DATABASE_URL=postgresql+psycopg2://postgres:your_password@localhost:5432/basic_rag
```

### 3. Start PostgreSQL and create the database

Make sure the PostgreSQL service is running, then create the database:

```powershell
"C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres -c "CREATE DATABASE basic_rag;"
```

If the database already exists, PostgreSQL will report that and you can continue.

### 4. Initialize the database tables

```powershell
.venv\Scripts\python.exe -m scripts.init_db
```

### 5. Build or rebuild the FAISS index

```powershell
.venv\Scripts\python.exe -m scripts.build_index
```

### 6. Run the app

```powershell
.venv\Scripts\python.exe app.py
```

## Demo Flow

For the final assignment demo, show this order:

1. `.env` exists and contains real values
2. PostgreSQL service is running
3. `python -m scripts.init_db`
4. `python -m scripts.build_index`
5. `python app.py`
6. Ask one medical question
7. Show retrieved chunks in the console
8. Show the final answer
9. Verify the inserted row in `qa_logs`

Example query:

```text
What are the symptoms of glaucoma?
```

## Verification Status In This Repo

These items are verified from the current codebase:

- Folder structure is present: `db/`, `rag/`, `scripts/`, `data/`
- `__init__.py` files exist where needed
- `.venv` exists in the project root
- `config.py` imports safely without crashing on unrelated missing variables
- Data loading, null filtering, document building, and chunking are implemented
- `scripts.test_medquad_preprocessing` runs successfully and produced:
  - `16,407` loaded documents
  - `61,886` chunks
- FAISS artifacts exist on disk:
  - `faiss_index/index.faiss`
  - `faiss_index/index.pkl`
- Retrieval, generation, and logging code paths are implemented

These items still require your real local credentials or services to verify:

- `.env` values are correct
- PostgreSQL login works
- `basic_rag` database exists
- `python -m scripts.init_db` completes successfully
- A real Gemini response is generated
- A demo question inserts a visible row into `qa_logs`

## Troubleshooting

### Missing `.env`

If you see a runtime error about `DATABASE_URL` or `GEMINI_API_KEY`, create `.env` from `.env.example` and replace placeholders with real values.

### PostgreSQL authentication failed

Check the password inside `DATABASE_URL`. Example format:

```env
DATABASE_URL=postgresql+psycopg2://postgres:your_password@localhost:5432/basic_rag
```

### `psql` is not recognized

Use the full executable path instead:

```powershell
"C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres -lqt
```

### SentenceTransformer model download issues

The embedding model may need network access the first time it is downloaded. After that, it should load from the local cache.

## Notes

- No secrets should be committed to git.
- Run scripts from the project root.
- The logger stores question, context, answer, timestamp, similarity scores, and retrieved chunk IDs.

## License

Educational assignment project.
