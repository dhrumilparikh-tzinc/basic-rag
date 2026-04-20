# Basic RAG (Retrieval Augmented Generation) Assignment

A Retrieval Augmented Generation system built with Python that loads medical Q&A data, chunks documents, and prepares them for semantic search and retrieval tasks.

## Project Structure

```
basic_rag_assignment/
├── app.py                      # Main application entry point
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── readme.md                   # This file
│
├── data/
│   └── medquad.csv            # Medical Q&A dataset (MedQuAD)
│
├── db/
│   ├── db.py                  # Database operations
│   └── models.py              # Database models
│
├── faiss_index/               # FAISS vector index storage
│
├── rag/
│   ├── __init__.py           # RAG package initialization
│   ├── loader.py             # Document loader for CSV data
│   ├── chunker.py            # Document chunking utilities
│   └── models.py             # RAG models and utilities
│
└── scripts/
    ├── download_kaggle_data.py      # Download MedQuAD dataset from Kaggle
    ├── inspect_medquad.py           # Inspect and analyze dataset columns
    └── test_medquad_preprocessing.py # Test data preprocessing pipeline
```

## Features Implemented

### 1. **Document Loading** (`rag/loader.py`)
- Loads medical Q&A data from CSV files
- Configurable column mapping (Question, Answer, Category)
- Handles missing values and data validation
- Returns processed documents as structured text

### 2. **Document Chunking** (`rag/chunker.py`)
- Splits long documents into overlapping chunks
- Configurable chunk size and overlap parameters
- Preserves context across chunks
- Supports batch processing of multiple documents

### 3. **Data Pipeline** (`scripts/`)
- **inspect_medquad.py**: Inspect dataset structure and columns
- **download_kaggle_data.py**: Download MedQuAD dataset from Kaggle
- **test_medquad_preprocessing.py**: Test preprocessing pipeline

### 4. **Database Layer** (`db/`)
- Database operations and management
- Models for storing documents and metadata
- Support for vector storage with FAISS

## Requirements

- Python 3.8+
- pandas
- numpy
- python-dotenv
- kaggle

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### 1. Download Data
```bash
python scripts/download_kaggle_data.py
```

### 2. Inspect Dataset
```bash
python scripts/inspect_medquad.py
```

### 3. Load and Process Documents
```python
from rag.loader import load_documents
from rag.chunker import chunk_documents

# Load documents from CSV
documents = load_documents()
print(f"Loaded {len(documents)} documents")

# Chunk documents for processing
chunks = chunk_documents(documents, chunk_size=500, overlap=100)
print(f"Created {len(chunks)} chunks")
```

## Configuration

Update `config.py` with your settings:
- Dataset paths
- Column mappings
- Chunking parameters
- Database connections
- Model configurations

## Project Status

✅ **Completed:**
- Project structure and organization
- Document loader implementation
- Document chunking system
- Data inspection scripts
- Requirements and dependencies

🔄 **In Progress / To Do:**
- Database models and operations
- FAISS index integration
- Embedding generation
- Retrieval functionality
- API/Application layer

## Next Steps

1. Implement embedding models (e.g., using sentence-transformers)
2. Create FAISS index for vector search
3. Build retrieval system
4. Implement API endpoints in `app.py`
5. Add evaluation metrics

## License

This project is part of a RAG assignment.
