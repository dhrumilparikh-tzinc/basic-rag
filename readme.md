# Medical RAG API

FastAPI service for medical question answering using retrieval-augmented generation (RAG).

## What It Does

- Retrieves relevant medical context from FAISS index
- Uses Gemini to generate an answer grounded in retrieved context
- Exposes simple REST endpoints for integration

## Project Structure

- `api.py` - FastAPI application
- `rag/` - Retriever and generator pipeline
- `db/` - Optional logging layer
- `data/medquad.csv` - Source dataset
- `faiss_index/` - Vector index files
- `Medical_RAG_API.postman_collection.json` - Postman collection

## Prerequisites

- Python 3.10+
- Virtual environment
- Gemini API key
- Optional: PostgreSQL if you want DB logging

## Environment

Create or update `.env`:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-2.5-flash
DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/basic_rag
```

## Install

```powershell
pip install -r requirements.txt
```

## Run API

```powershell
python -m uvicorn api:app --host 127.0.0.1 --port 8000
```

If port 8000 is already in use, close old server process and run again.

## Endpoints

- `GET /` - API info
- `GET /health` - health check
- `POST /ask` - full response with chunks
- `POST /ask/simple` - short response

## Request Example

```json
{
  "question": "What are the symptoms of diabetes?",
  "k": 3
}
```

## Response Notes

- `200` - success
- `422` - invalid/missing body (usually Postman Body tab not set to raw JSON)
- `500/503` - upstream model/provider temporary issue

## Postman

1. Import `Medical_RAG_API.postman_collection.json`
2. Start with `GET /health`
3. Use `POST /ask` with `Content-Type: application/json`
4. In Body tab choose `raw` + `JSON`

## Quick Troubleshooting

- `ECONNREFUSED`: API server not running
- `422 Unprocessable Content`: request body missing or invalid JSON
- `405 Method Not Allowed`: wrong HTTP method (for example GET on `/ask`)
- `503 Service Unavailable`: Gemini is under high load, retry shortly

## License

Internal assignment use.
# Medical RAG API - Shareable Endpoint

**A production-ready REST API for medical Q&A powered by Retrieval-Augmented Generation.**

Share this API with anyone to integrate AI-powered medical question answering into their applications.

## ⭐ Key Features

- **REST API Endpoints** - Easy to integrate into any application
- **Medical Q&A** - Powered by FAISS vector search + Google Gemini LLM
- **Grounded Answers** - Includes retrieved context chunks with sources
- **PostgreSQL Logging** - Audit trail of all interactions
- **Production Ready** - Error handling, validation, documentation
- **No UI** - Pure API, easy to integrate anywhere
- **Well Documented** - Integration guides for Python, JavaScript, cURL
- **Self-Hostable** - Deploy on your own servers

---

## 🚀 Quick Navigation

### 📖 For Users/Integrators
Start with **[API_README.md](API_README.md)** for a quick overview.

### 💻 For Developers Integrating
See **[INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md)** for code examples in Python, JavaScript, and cURL.

### 🏗 For Deployment
Check **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** for production setup.

### 🎯 For Sharing
Read **[SHARING_GUIDE.md](SHARING_GUIDE.md)** on what to share with others.

### 🧪 For Testing
Import **[Medical_RAG_API.postman_collection.json](Medical_RAG_API.postman_collection.json)** into Postman.

---

## 🎯 API Endpoints

```bash
# Health check
GET /health

# Ask a medical question (full response with chunks)
POST /ask
{
  "question": "What are the symptoms of diabetes?",
  "k": 5
}

# Quick answer (simple response)
POST /ask/simple
{
  "question": "How to treat high blood pressure?"
}
```

---

## 📋 Setup (Quick Start)

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

##Output

<img width="1548" height="913" alt="image" src="https://github.com/user-attachments/assets/8a91d3cd-725e-4e04-8c92-b2afccdc56b9" />

<img width="1560" height="965" alt="image" src="https://github.com/user-attachments/assets/96e97317-8135-4034-bfd8-95b5907d0dd0" />

<img width="1577" height="971" alt="image" src="https://github.com/user-attachments/assets/a270407c-c5c9-48b6-baee-0568ddbbee97" />



## License

Educational assignment project.
