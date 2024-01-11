 clus = faiss.Clustering(d, n_fine_clusters)
clus.train(data, index)
centroids = faiss.vector_float_to_array(clus.centroids).reshape(n_fine_clusters, d)

fine_quantizers = [faiss.IndexFlatL2(d) for _ in range(n_coarse_clusters)]
for i in range(n_coarse_clusters):
    mask = index.assign(data, 1) == i
    fine_quantizers[i].add(data[mask])


