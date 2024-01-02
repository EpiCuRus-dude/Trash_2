import numpy as np
from scipy.cluster.hierarchy import ward, fcluster
from scipy.spatial.distance import pdist, euclidean
from collections import defaultdict

# Assuming X is your matrix of embeddings and 'categories' is the list of category labels

def hierarchical_clustering(embeddings, threshold):
    linkage_matrix = ward(pdist(embeddings))
    return fcluster(linkage_matrix, threshold, criterion='distance')

def compute_centroids(embeddings, labels):
    unique_labels = np.unique(labels)
    return np.array([embeddings[labels == label].mean(axis=0) for label in unique_labels])

def compute_weighted_labels(embeddings, labels, categories, centroids):
    cluster_category_weights = defaultdict(lambda: defaultdict(float))

    for i, (emb, label) in enumerate(zip(embeddings, labels)):
        category = categories[i]
        centroid = centroids[label - 1]  
        distance = euclidean(emb, centroid)
        weight = 1 / (distance + 1e-5)  
        cluster_category_weights[label][category] += weight

    
    weighted_labels = {}
    for label, category_weights in cluster_category_weights.items():
        weighted_labels[label] = max(category_weights, key=category_weights.get)

    return weighted_labels


threshold = 1.5
cluster_labels = hierarchical_clustering(X, threshold)


centroids = compute_centroids(X, cluster_labels)


centroid_labels = compute_weighted_labels(X, cluster_labels, categories, centroids)



nearest_cluster_index, _ = find_nearest_cluster(query_embedding, faiss_index)
nearest_cluster_category = centroid_labels[nearest_cluster_index + 1] 
print("Nearest Cluster Category:", nearest_cluster_category)
