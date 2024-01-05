


#nothing special, make an index for each cluster!

def create_embeddings(data):
    
    ... # whatever

def train_kmeans(embeddings, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters, random_state=0)
    kmeans.fit(embeddings)
    return kmeans

def cfai_ind(embeddings, kmeans):
    n_clusters = kmeans.n_clusters
    faiss_indexes = [faiss.IndexFlatL2(embeddings.shape[1]) for _ in range(n_clusters)]

    for i, embedding in enumerate(embeddings):
        cluster_id = kmeans.labels_[i]
        faiss_indexes[cluster_id].add(np.array([embedding]))

    return faiss_indexes

def search(query_embedding, kmeans, faiss_indexes, k=10):
    
    nearest_cluster = kmeans.predict(np.array([query_embedding]))[0]

    
    distances, indices = faiss_indexes[nearest_cluster].search(np.array([query_embedding]), k)
    return distances, indices


