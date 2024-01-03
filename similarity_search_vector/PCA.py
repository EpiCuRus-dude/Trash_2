import numpy as np
import faiss
from sklearn.decomposition import PCA


d = 128  
nb = 9000  
np.random.seed(1234)
db_vectors = np.random.random((nb, d)).astype('float32')

# Dimensionality reduction using PCA
new_d = 64  #
pca = PCA(n_components=new_d)
db_vectors_reduced = pca.fit_transform(db_vectors)


db_vectors_reduced = db_vectors_reduced.astype('float32')


index = faiss.IndexFlatL2(new_d)


index.add(db_vectors_reduced)


query_vector = np.random.random((1, d)).astype('float32')
query_vector_reduced = pca.transform(query_vector).astype('float32')


k = 4  
D, I = index.search(query_vector_reduced, k) 
