import numpy as np
from sklearn.decomposition import PCA

def calculate_pca_weights(results):
    pca = PCA(n_components=2)
    pca.fit(results)
    explained_variances = pca.explained_variance_ratio_
    return explained_variances.sum()

all_results = [
    np.random.rand(10, 128),
    np.random.rand(10, 128),
    np.random.rand(10, 128)
]

pca_weights = [calculate_pca_weights(results) for results in all_results]
pca_weights_normalized = np.array(pca_weights) / np.sum(pca_weights)

print("Weights based on PCA explained variance:", pca_weights_normalized)
