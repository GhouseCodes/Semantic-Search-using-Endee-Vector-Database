import faiss
import numpy as np

dimension = 384
index = faiss.IndexFlatL2(dimension)
documents = []

def add_vectors(vectors, texts):
    global documents
    index.add(np.array(vectors).astype("float32"))
    documents.extend(texts)

def search_vector(vector, top_k=3):
    D, I = index.search(np.array([vector]).astype("float32"), top_k)
    results = []
    for idx in I[0]:
        if idx < len(documents):
            results.append(documents[idx])
    return results
