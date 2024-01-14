from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


sentence1 = "I have a cat"
sentence2 = "I have a dog"


vectorizer = CountVectorizer()
X = vectorizer.fit_transform([sentence1, sentence2]).toarray()


euclidean_distance = np.linalg.norm(X[0] - X[1])


cos_sim = cosine_similarity([X[0]], [X[1]])[0][0]

print("Euclidean Distance:", euclidean_distance)
print("Cosine Similarity:", cos_sim)
