import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def calculate_pca_explained_variance(embeddings, n_components=10):
    pca = PCA(n_components=n_components)
    pca.fit(embeddings)
    return pca.explained_variance_ratio_


def plot_cumulative_explained_variance(explained_variance, title):
    cumulative_variance = np.cumsum(explained_variance)
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o', label=title)
    plt.xlabel('Number of Principal Components')
    plt.ylabel('Cumulative Explained Variance')
    plt.title(f'Cumulative Explained Variance - {title}')
    plt.legend()
    plt.grid(True)
    plt.show()


def compute_reconstruction_error(embeddings, pca):
    reconstructed = pca.inverse_transform(pca.transform(embeddings))
    reconstruction_error = np.mean((embeddings - reconstructed) ** 2)
    return reconstruction_error




pca_explained_variance_llm1 = calculate_pca_explained_variance(embeddings_llm1, n_components=10)
cumulative_variance_llm1 = np.cumsum(pca_explained_variance_llm1)
print("LLM1 Cumulative Explained Variance:", cumulative_variance_llm1)


pca_explained_variance_llm2 = calculate_pca_explained_variance(embeddings_llm2, n_components=10)
cumulative_variance_llm2 = np.cumsum(pca_explained_variance_llm2)
print("LLM2 Cumulative Explained Variance:", cumulative_variance_llm2)


plot_cumulative_explained_variance(pca_explained_variance_llm1, 'LLM1')
plot_cumulative_explained_variance(pca_explained_variance_llm2, 'LLM2')


def find_elbow_point(cumulative_variance):
    n_components = len(cumulative_variance)
    diffs = np.diff(cumulative_variance)
    elbow_point = np.argmax(diffs[1:] - diffs[:-1]) + 1
    return elbow_point


elbow_llm1 = find_elbow_point(cumulative_variance_llm1)
elbow_llm2 = find_elbow_point(cumulative_variance_llm2)

print(f"LLM1 Elbow Point: {elbow_llm1}")
print(f"LLM2 Elbow Point: {elbow_llm2}")
