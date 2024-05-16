import numpy as np
import matplotlib.pyplot as plt

def kneedle(scores):
    sorted_indices = np.argsort(scores)[::-1]
    sorted_scores = scores[sorted_indices]
    cumulative_scores = np.cumsum(sorted_scores)
    normalized_cumulative_scores = cumulative_scores / cumulative_scores[-1]
    
    differences = np.diff(normalized_cumulative_scores)
    diff_signs = np.sign(differences)
    knee_point = np.argmax(diff_signs < 0) + 1
    
    return knee_point, sorted_indices[:knee_point]

scores = np.array([85, 92, 88, 96, 80, 78, 84, 93, 91, 87])
optimal_candidates, top_indices = kneedle(scores)

print(f"Optimal number of top candidates to choose: {optimal_candidates}")
print(f"Indices of top candidates: {top_indices}")
print(f"Top candidates' scores: {scores[top_indices]}")

sorted_scores = np.sort(scores)[::-1]
cumulative_scores = np.cumsum(sorted_scores)
normalized_cumulative_scores = cumulative_scores / cumulative_scores[-1]
plt.plot(range(1, len(scores) + 1), normalized_cumulative_scores, marker='o')
plt.axvline(x=optimal_candidates, color='r', linestyle='--')
plt.xlabel('Number of Candidates')
plt.ylabel('Normalized Cumulative Score')
plt.title('Kneedle Method for Optimal Number of Candidates')
plt.show()
