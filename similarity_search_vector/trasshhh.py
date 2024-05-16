import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

def silhouette_method(scores):
    sorted_indices = np.argsort(scores)[::-1]
    sorted_scores = scores[sorted_indices]
    silhouette_scores = []
    
    for i in range(2, len(scores)):
        labels = np.zeros(len(scores))
        labels[:i] = 1
        silhouette_avg = silhouette_score(scores.reshape(-1, 1), labels)
        silhouette_scores.append(silhouette_avg)
    
    optimal_candidates = np.argmax(silhouette_scores) + 2
    top_indices = sorted_indices[:optimal_candidates]
    
    return optimal_candidates, top_indices, silhouette_scores

scores = np.array([85, 92, 88, 96, 80, 78, 84, 93, 91, 87])
optimal_candidates, top_indices, silhouette_scores = silhouette_method(scores)

print(f"Optimal number of top candidates to choose: {optimal_candidates}")
print(f"Indices of top candidates: {top_indices}")
print(f"Top candidates' scores: {scores[top_indices]}")

plt.plot(range(2, len(scores)), silhouette_scores, marker='o')
plt.axvline(x=optimal_candidates, color='r', linestyle='--')
plt.xlabel('Number of Top Candidates')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Method for Optimal Number of Top Candidates')
plt.show()
