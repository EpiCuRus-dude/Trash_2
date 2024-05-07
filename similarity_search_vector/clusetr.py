from sklearn.cluster import KMeans

def cluster_coherence(results):
    kmeans = KMeans(n_clusters=3)  
    labels = kmeans.fit_predict(results)
    
    coherence = kmeans.inertia_
    return coherence

coherences = [cluster_coherence(results) for results in all_results]
coherence_weights = np.array(coherences)
coherence_weights = 1 / coherence_weights  
coherence_weights /= np.sum(coherence_weights)

print("Weights based on cluster coherence:", coherence_weights)
