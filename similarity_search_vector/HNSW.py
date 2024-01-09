dim = data.shape[1]


index = faiss.IndexHNSWFlat(dim, 32)  


index.train(data)


index.add(data)


distances, indices = index.search(query, k)
