import numpy as np
from sklearn.decomposition import PCA

# Scores from 3 recommenders for 5 candidates
scores = np.array([
    [0.9, 0.1, 0.2],
    [0.5, 0.6, 0.7],
    [0.3, 0.4, 0.5],
    [0.8, 0.8, 0.1],
    [0.2, 0.2, 0.9]
])


pca = PCA(n_components=1)  # Reduce to 1 component for simplicity
principal_components = pca.fit_transform(scores.T)  # Transpose to have recommenders as rows


weights = np.abs(principal_components.ravel())
weights /= np.sum(weights)  # Normalize weights


weighted_scores = scores.dot(weights)

print("Weights based on PCA:", weights)
print("Weighted Scores:", weighted_scores)
