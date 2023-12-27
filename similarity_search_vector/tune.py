import faiss
import numpy as np

# Let's assume we have a dataset of 128-dimensional vectors
d = 128           # dimension
nb = 10000        # database size
nq = 100          # number of queries
np.random.seed(1234) 

# Randomly generating the database and query vectors
xb = np.random.random((nb, d)).astype('float32')
xb[:, 0] += np.arange(nb) / 1000.  # To make vectors more distinct
xq = np.random.random((nq, d)).astype('float32')
xq[:, 0] += np.arange(nq) / 1000. 

# Normalizing the vectors to unit length for IndexFlatIP (cosine similarity)
xb_norm = xb / np.linalg.norm(xb, axis=1)[:, np.newaxis]
xq_norm = xq / np.linalg.norm(xq, axis=1)[:, np.newaxis]

# Creating the index
index = faiss.IndexFlatIP(d)  # IndexFlatIP for Inner Product (cosine similarity)

# Adding the vectors to the index
index.add(xb_norm)

# Searching
k = 4  # We want to see 4 nearest neighbors
D, I = index.search(xq_norm, k)  # D: distances, I: indices of the nearest neighbors

# Displaying the results for the first 5 queries
for i in range(5):
    print(f"Query {i}")
    print(f"Nearest neighbors: {I[i]}")
    print(f"Distances: {D[i]}\n")


nlist = 100  # Number of Voronoi cells
quantizer = faiss.IndexFlatIP(d)  # We keep the same quantizer
index_ivf = faiss.IndexIVFFlat(quantizer, d, nlist, faiss.METRIC_INNER_PRODUCT)


assert not index_ivf.is_trained
index_ivf.train(xb_norm)
assert index_ivf.is_trained


index_ivf.add(xb_norm)


nprobe = 10  
index_ivf.nprobe = nprobe


D_ivf, I_ivf = index_ivf.search(xq_norm, k)


for i in range(5):
    print(f"Query {i} (IVF)")
    print(f"Nearest neighbors: {I_ivf[i]}")
    print(f"Distances: {D_ivf[i]}\n")



