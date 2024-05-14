from sklearn.cluster import KMeans

def kmeans_top_cluster(scores, n_clusters=3):
    scores = scores.reshape(-1, 1)  # Reshape for clustering
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(scores)
    cluster_centers = kmeans.cluster_centers_
    top_cluster_center = np.max(cluster_centers)
    top_cluster_label = np.where(cluster_centers == top_cluster_center)[0][0]
    return scores[kmeans.labels_ == top_cluster_label].flatten()


top_candidates = kmeans_top_cluster(scores)
