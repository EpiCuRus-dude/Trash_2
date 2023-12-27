import faiss
import numpy as np

def normalize_vectors(vectors):
    
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    return vectors / np.maximum(norms, 1e-6)

def create_index(vector_dim):
    
    return faiss.IndexFlatIP(vector_dim)

def add_vectors_to_index(index, vectors):
   
    normalized_vectors = normalize_vectors(vectors)
    index.add(normalized_vectors)

def search_vectors(index, query_vectors, k):
    
    normalized_query_vectors = normalize_vectors(query_vectors)
    return index.search(normalized_query_vectors, k)

# Example usage
vector_dim = 128  
num_vectors = 1000  
k = 10  

np.random.seed(123)
db_vectors = np.random.random((num_vectors, vector_dim)).astype('float32')
query_vectors = np.random.random((5, vector_dim)).astype('float32')


index = create_index(vector_dim)

add_vectors_to_index(index, db_vectors)


D, I = search_vectors(index, query_vectors, k)

print("Distances (cosine similarities):", D)
print("Indices:", I)
