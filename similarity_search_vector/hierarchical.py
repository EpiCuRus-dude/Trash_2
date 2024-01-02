from scipy.cluster.hierarchy import ward, fcluster
from scipy.spatial.distance import pdist

def hierarchical_clustering(embeddings, threshold):
    
    linkage_matrix = ward(pdist(embeddings))

    labels = fcluster(linkage_matrix, threshold, criterion='distance')
    return labels


threshold = 1.5  


labels = {}
for category, emb in embeddings.items():
    labels[category] = hierarchical_clustering(emb, threshold)


def compute_centroids(embeddings, labels):
    unique_labels = np.unique(labels)
    centroids = np.array([embeddings[labels == label].mean(axis=0) for label in unique_labels])
    return centroids


centroids = {}
for category, emb in embeddings.items():
    centroids[category] = compute_centroids(emb, labels[category])


faiss_indices = {}
for category, centers in centroids.items():
    faiss_indices[category] = create_faiss_index(centers.astype('float32'))


query_embedding = np.random.rand(1, 128).astype('float32')
nearest_category = find_nearest_category(query_embedding, faiss_indices)
print("Nearest Category:", nearest_category)


