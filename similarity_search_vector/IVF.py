nlist = 100  
quantizer = faiss.IndexFlatL2(d)  
index = faiss.IndexIVFFlat(quantizer, d, nlist, faiss.METRIC_L2)


assert not index.is_trained
index.train(db_vectors)
assert index.is_trained

index.add(db_vectors)

