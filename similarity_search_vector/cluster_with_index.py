import faiss
import numpy as np


d = 128  
nb = 1000  
np.random.seed(1234)
db_vectors = np.random.random((nb, d)).astype('float32')


nlist = 100  
m = 8  
quantizer = faiss.IndexFlatL2(d)  
index = faiss.IndexIVFPQ(quantizer, d, nlist, m, 8)


index.train(db_vectors)


index.add(db_vectors)


nprobe = 10  
index.nprobe = nprobe

k = 4  
query_vector = np.random.random((1, d)).astype('float32')
D, I = index.search(query_vector, k)  # Distance and Index of neighbors
