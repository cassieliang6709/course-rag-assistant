# Course RAG Assistant

Retrieval-augmented course assistant that answers questions from lecture notes, assignments, and readings with citations.

## Technical Highlights

- RAG pipeline design
- Retrieval evaluation
- Prompt and answer quality testing
- Clean separation between indexing, retrieval, and generation

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```
