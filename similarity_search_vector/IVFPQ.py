import faiss

d = ...
nlist = ...
m = 8  


quantizer = faiss.IndexFlatIP(d)


index = faiss.IndexIVFPQ(quantizer, d, nlist, m, 8)
index.metric_type = faiss.METRIC_INNER_PRODUCT  


index.train(concatenated_vectors)


index.add(concatenated_vectors)
