from fastapi import FastAPI
from .indexer import index_documents
from .embed import create_embedding
from .vector_store import search_vector

app = FastAPI()

@app.on_event("startup")
def startup():
    index_documents()

@app.get("/")
def root():
    return {"message": "Semantic Search API is running"}

@app.get("/search")
def search(q: str):
    emb = create_embedding(q)
    results = search_vector(emb)
    return {"query": q, "results": results}
