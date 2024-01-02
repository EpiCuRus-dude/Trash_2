# Does it work?

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import faiss
from sklearn.cluster import AgglomerativeClustering
from collections import Counter


paper_titles = ["Title 1", "Title 2", ...]  
categories = ["Math", "Physics", ...]  


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(paper_titles).toarray()


index = faiss.IndexFlatL2(X.shape[1])
index.add(X.astype(np.float32))

def predict_category_hierarchical(new_title, k=10):
    
    new_vector = vectorizer.transform([new_title]).toarray().astype(np.float32)
    
    
    _, indices = index.search(new_vector, k)
    
    
    neighbor_embeddings = X[indices[0]]

    
    cluster = AgglomerativeClustering(n_clusters=None, distance_threshold=0.5, linkage='ward')
    cluster.fit(neighbor_embeddings)

    
    neighbor_categories = np.array([categories[idx] for idx in indices[0]])

    
    cluster_categories = {}
    for cluster_id in np.unique(cluster.labels_):
        cluster_member_categories = neighbor_categories[cluster.labels_ == cluster_id]
        most_common_category = Counter(cluster_member_categories).most_common(1)[0][0]
        cluster_categories[cluster_id] = most_common_category

    
    largest_cluster_id = Counter(cluster.labels_).most_common(1)[0][0]
    predicted_category = cluster_categories[largest_cluster_id]

    return predicted_category


new_title = "A New Research Paper on Quantum Physics"
predicted_category = predict_category_hierarchical(new_title, k=10)
print(f"The predicted category for '{new_title}' is '{predicted_category}'")
