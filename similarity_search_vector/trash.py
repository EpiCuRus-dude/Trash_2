import faiss
import numpy as np

def create_index(vector_dim):
    
    return faiss.IndexFlatIP(vector_dim)

def add_vectors_to_index(index, vectors):
    
    faiss.normalize_L2(vectors)  # Normalize the vectors in-place
    index.add(vectors)

def search_vectors(index, query_vectors, k):
    
    faiss.normalize_L2(query_vectors)  # Normalize the query vectors in-place
    return index.search(query_vectors, k)


vector_dim = 128  # Dimension of the vectors
num_vectors = 1000  # Number of vectors in the database
k = 10  # Number of nearest neighbors to find


np.random.seed(123)
db_vectors = np.random.random((num_vectors, vector_dim)).astype('float32')
query_vectors = np.random.random((5, vector_dim)).astype('float32')


index = create_index(vector_dim)


add_vectors_to_index(index, db_vectors)


D, I = search_vectors(index, query_vectors, k)

print("Distances (cosine similarities):", D)
print("Indices:", I)
