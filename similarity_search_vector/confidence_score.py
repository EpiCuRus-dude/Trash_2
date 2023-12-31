import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import faiss
from collections import defaultdict


paper_titles = ["Title 1", "Title 2", ...]  
categories = ["Math", "Physics", ...]  


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(paper_titles).toarray()


index = faiss.IndexFlatL2(X.shape[1])
index.add(X.astype(np.float32))

def calculate_confidence_scores(distances, indices):
    
    confidence_scores = defaultdict(float)

    
    for distance, idx in zip(distances[0], indices[0]):
        category = categories[idx]
        
        confidence_scores[category] += 1 / (1 + distance)

    return confidence_scores

def predict_category_with_confidence(new_title, k=10):
    
    new_vector = vectorizer.transform([new_title]).toarray().astype(np.float32)
    
    
    distances, indices = index.search(new_vector, k)
    
    
    confidence_scores = calculate_confidence_scores(distances, indices)

    
    predicted_category = max(confidence_scores, key=confidence_scores.get)
    return predicted_category


new_title = "A New Research Paper on Quantum Physics"
predicted_category = predict_category_with_confidence(new_title, k=10)
print(f"The predicted category for '{new_title}' is '{predicted_category}'")
