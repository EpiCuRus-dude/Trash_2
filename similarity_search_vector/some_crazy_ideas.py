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

import numpy as np


scores = np.array([
    [0.9, 0.1, 0.2],
    [0.5, 0.6, 0.7],
    [0.3, 0.4, 0.5],
    [0.8, 0.8, 0.1],
    [0.2, 0.2, 0.9]
])


variances = np.var(scores, axis=0)


weights = 1 / variances
weights /= np.sum(weights)  # Normalize weights to sum to 1


weighted_scores = np.dot(scores, weights)

print("Weights:", weights)
print("Weighted Scores:", weighted_scores)


import numpy as np

# Scores from 3 recommenders for 5 candidates
scores = np.array([
    [0.9, 0.1, 0.2],
    [0.5, 0.6, 0.7],
    [0.3, 0.4, 0.5],
    [0.8, 0.8, 0.1],
    [0.2, 0.2, 0.9]
])


def entropy(scores):
    p = scores / np.sum(scores)
    return -np.sum(p * np.log(p + 1e-9))  # Adding a small number to prevent log(0)


entropies = np.array([entropy(scores[:, i]) for i in range(scores.shape[1])])


weights = entropies / np.sum(entropies)


weighted_scores = scores.dot(weights)

print("Entropy-based Weights:", weights)
print("Weighted Scores:", weighted_scores)



import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.utils import resample

# Example data: scores from 3 recommenders for 5 candidates
from sklearn.preprocessing import StandardScaler
from sklearn.utils import resample
scores = np.array([
    [0.9, 0.1, 0.2],
    [0.5, 0.6, 0.7],
    [0.3, 0.4, 0.5],
    [0.8, 0.8, 0.1],
    [0.2, 0.2, 0.9]
])


scaler = StandardScaler()
scores_standardized = scaler.fit_transform(scores)


pca = PCA()
components = pca.fit_transform(scores_standardized.T)  


explained_variance = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance)
n_components = np.where(cumulative_variance >= 0.8)[0][0] + 1 


loadings = pca.components_[:n_components, :]
weights = np.sum(loadings, axis=0)
weights /= np.sum(weights) 


weighted_scores = np.dot(scores, weights)

print("PCA-derived Weights:", weights)
print("Weighted Scores:", weighted_scores)


