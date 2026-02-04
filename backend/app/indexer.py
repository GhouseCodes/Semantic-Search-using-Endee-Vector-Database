from .embed import create_embedding
from .vector_store import add_vectors

DOCUMENTS = [
    "AI is transforming software development",
    "Vector databases store embeddings for search",
    "FastAPI is a modern Python web framework",
    "Machine learning is fun to learn",
    "Semantic search finds meaning, not keywords"
]

def index_documents():
    vectors = []
    texts = []

    for doc in DOCUMENTS:
        emb = create_embedding(doc)
        vectors.append(emb)
        texts.append(doc)

    add_vectors(vectors, texts)
    print("Documents indexed successfully")
