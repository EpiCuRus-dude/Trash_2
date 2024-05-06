import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

data = np.array([
    [8.0, 0.64],
    [7.5, 0.09],
    [8.5, 0.49]
])

scaler = StandardScaler()
data_normalized = scaler.fit_transform(data)

pca = PCA(n_components=1)
pca.fit(data_normalized)

weights = pca.components_[0]
weights_normalized = weights / np.sum(weights)
weights_normalized
