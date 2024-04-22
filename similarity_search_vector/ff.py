import faiss


d = data_normalized.shape[1] 
nlist = 4096 
m = 8     





quantizer = faiss.IndexFlatL2(d) 
index = faiss.IndexIVFPQ(quantizer, d, nlist, m, 8) 

# Train the index with a subset of the data (e.g., 100k samples)
index.train(data_normalized[:100_000])

