from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np


encoding_1 = np.random.rand(10, 300)
encoding_2 = np.random.rand(10, 768)


scaler = StandardScaler()
pca = PCA(n_components=200)

normalized_encoding_1 = scaler.fit_transform(encoding_1)
pca_encoding_1 = pca.fit_transform(normalized_encoding_1)

normalized_encoding_2 = scaler.fit_transform(encoding_2)
pca_encoding_2 = pca.fit_transform(normalized_encoding_2)




combined_encoding = np.concatenate((pca_encoding_1, pca_encoding_2, ...), axis=1)
