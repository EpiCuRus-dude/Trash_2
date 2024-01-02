from scipy.cluster.hierarchy import ward, fcluster
from scipy.spatial.distance import pdist

def hierarchical_clustering(embeddings, threshold):
    
    linkage_matrix = ward(pdist(embeddings))
    # Form clusters based on a distance threshold
    labels = fcluster(linkage_matrix, threshold, criterion='distance')
    return labels


threshold = 1.5  
cluster_labels = hierarchical_clustering(X, threshold)
def compute_centroids(embeddings, labels):
    unique_labels = np.unique(labels)
    centroids = np.array([embeddings[labels == label].mean(axis=0) for label in unique_labels])
    return centroids

centroids = compute_centroids(X, cluster_labels)

import faiss

def create_faiss_index(vectors):
    dimension = vectors.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(vectors.astype('float32'))
    return index

faiss_index = create_faiss_index(centroids)

def find_nearest_cluster(query_embedding, faiss_index):
    distances, indices = faiss_index.search(query_embedding.astype('float32'), 1)
    return indices[0][0], distances[0][0]


query_embedding = np.random.rand(1, 2048)


from collections import Counter

def compute_centroids_and_labels(embeddings, labels, categories):
    unique_labels = np.unique(labels)
    centroids = []
    centroid_labels = []

    for label in unique_labels:
        
        cluster_embeddings = embeddings[labels == label]

        
        centroid = cluster_embeddings.mean(axis=0)
        centroids.append(centroid)

        
        cluster_categories = [categories[i] for i in range(len(categories)) if labels[i] == label]
        most_common_category = Counter(cluster_categories).most_common(1)[0][0]
        centroid_labels.append(most_common_category)

    return np.array(centroids), centroid_labels



nearest_cluster_index, distance = find_nearest_cluster(query_embedding, faiss_index)
print("Nearest Cluster Index:", nearest_cluster_index, "Distance:", distance)




categories = ["math", "physics", "chemistry", ...]  


centroids, centroid_labels = compute_centroids_and_labels(X, cluster_labels, categories)

nearest_cluster_index, _ = find_nearest_cluster(query_embedding, faiss_index)
nearest_cluster_category = centroid_labels[nearest_cluster_index]
print("Nearest Cluster Category:", nearest_cluster_category)


