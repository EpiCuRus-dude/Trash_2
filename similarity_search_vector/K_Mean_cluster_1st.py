import numpy as np
import faiss
from sklearn.cluster import KMeans


n_clusters = 10  # number of clusters
kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(data)
labels = kmeans.labels_

faiss_indexes = []
for i in range(n_clusters):
    cluster_data = data[labels == i]
    index = faiss.IndexFlatL2(128)  # using FLATL2 index
    index.add(cluster_data)
    faiss_indexes.append(index)



distances, indices = kmeans.transform([query_vector]), kmeans.predict([query_vector])


results = []
for idx in indices[0][:n_search_clusters]:
    D, I = faiss_indexes[idx].search(np.array([query_vector]), top_k)
    results.extend([(idx, i, d) for i, d in zip(I[0], D[0])])


results.sort(key=lambda x: x[2])


