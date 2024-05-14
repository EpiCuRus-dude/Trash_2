from sklearn.cluster import KMeans

def kmeans_top_cluster_with_indices(scores, n_clusters=3):
    scores_reshaped = scores.reshape(-1, 1)  # Reshape for clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    kmeans.fit(scores_reshaped)
    cluster_centers = kmeans.cluster_centers_
    top_cluster_center = np.max(cluster_centers)
    top_cluster_label = np.where(cluster_centers == top_cluster_center)[0][0]
    
    top_candidates = scores[kmeans.labels_ == top_cluster_label]
    top_indices = np.where(kmeans.labels_ == top_cluster_label)[0]
    
    return top_candidates, top_indices


top_candidates, top_indices = kmeans_top_cluster_with_indices(scores)
top_candidates, top_indices
