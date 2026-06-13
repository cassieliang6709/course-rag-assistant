from fastapi import FastAPI

app = FastAPI(title="Course RAG Assistant")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
