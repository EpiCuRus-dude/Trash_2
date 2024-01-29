import faiss
import numpy as np


num_indices = 3
num_vectors = 1000  
vector_dim = 128    
top_k = 5           
np.random.seed(42)  


indices = [faiss.IndexFlatL2(vector_dim) for _ in range(num_indices)]
data = [np.random.random((num_vectors, vector_dim)).astype('float32') for _ in range(num_indices)]
for index, d in zip(indices, data):
    index.add(d)


query_vector = np.random.random((1, vector_dim)).astype('float32')


top_k_results = {}
for i, index in enumerate(indices, 1):
    _, distances = index.search(query_vector, top_k)
    top_k_results[f'Index_{i}'] = distances.flatten()

print("Top-k distances from each index:", top_k_results)
