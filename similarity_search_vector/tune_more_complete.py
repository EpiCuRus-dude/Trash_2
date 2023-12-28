import pandas as pd
import faiss
import numpy as np


train_data = pd.read_csv('train.csv').values.astype('float32')
test_data = pd.read_csv('test.csv').values.astype('float32')


train_data_norm = train_data / np.linalg.norm(train_data, axis=1)[:, np.newaxis]
test_data_norm = test_data / np.linalg.norm(test_data, axis=1)[:, np.newaxis]


d = train_data.shape[1]  # Dimension of vectors
nlist = 100              # Number of clusters for IVF index


quantizer = faiss.IndexFlatL2(d)  # Using L2 distance for the quantizer
index = faiss.IndexIVFFlat(quantizer, d, nlist, faiss.METRIC_L2)


if not index.is_trained:
    index.train(train_data_norm)


index.add(train_data_norm)


k = 5  # Number of nearest neighbors to find


D, I = index.search(test_data_norm, k)


for i in range(5):  # Show results for first 5 queries
    print(f"Query {i}")
    print(f"Nearest neighbors: {I[i]}")
    print(f"Distances: {D[i]}\n")
