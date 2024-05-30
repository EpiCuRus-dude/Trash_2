def calculate_variances(embeddings_list):
    variances = [np.var(embed) for embed in embeddings_list]
    return variances

variances = calculate_variances(embeddings)
print("Variances:", variances)


def calculate_overlap(embeddings_list):
    n = len(embeddings_list)
    overlap_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            distance = pairwise_distances(embeddings_list[i], embeddings_list[j], metric='cosine')
            average_distance = np.mean(distance)
            overlap_matrix[i][j] = overlap_matrix[j][i] = average_distance
    return overlap_matrix

overlap = calculate_overlap(embeddings)
print("Overlap matrix:\n", overlap)


def evaluate_diversity(embeddings_list, n_clusters=10):
    diversity_scores = []
    for embed in embeddings_list:
        kmeans = KMeans(n_clusters=n_clusters)
        kmeans.fit(embed)
        # Calculate diversity as the mean distance between cluster centers
        cluster_distances = pairwise_distances(kmeans.cluster_centers_)
        mean_distance = np.mean(cluster_distances)
        diversity_scores.append(mean_distance)
    return diversity_scores

diversity_scores = evaluate_diversity(embeddings)
print("Diversity Scores:", diversity_scores)

def perform_pca(embeddings_list, n_components=2):
    pca_results = []
    for embed in embeddings_list:
        pca = PCA(n_components=n_components)
        components = pca.fit_transform(embed)
        explained_variance = pca.explained_variance_ratio_.sum()
        pca_results.append((components, explained_variance))
    return pca_results

pca_analysis = perform_pca(embeddings)
for idx, result in enumerate(pca_analysis):
    print(f"Index {idx+1} PCA explained variance:", result[1])


