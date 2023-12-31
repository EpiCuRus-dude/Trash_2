import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import faiss
from collections import Counter


paper_titles = ["Title 1", "Title 2", ...]  
categories = ["Math", "Physics", ...] 


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(paper_titles).toarray()


index = faiss.IndexFlatL2(X.shape[1])
index.add(X.astype(np.float32))

def predict_category_weighted(new_title, k=5):
    
    new_vector = vectorizer.transform([new_title]).toarray().astype(np.float32)
    
    
    distances, indices = index.search(new_vector, k)
    
    
    weights = 1 / (1 + distances[0])  

    
    category_weights = {}
    for idx, weight in zip(indices[0], weights):
        cat = categories[idx]
        category_weights[cat] = category_weights.get(cat, 0) + weight

    
    predicted_category = max(category_weights, key=category_weights.get)
    return predicted_category


new_title = "A New Research Paper on Quantum Physics"
predicted_category = predict_category_weighted(new_title, k=5)
print(f"The predicted category for '{new_title}' is '{predicted_category}'")
