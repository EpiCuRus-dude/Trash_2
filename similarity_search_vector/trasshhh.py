import numpy as np
import matplotlib.pyplot as plt

def find_elbow_point(scores):
    sorted_indices = np.argsort(scores)[::-1]
    sorted_scores = scores[sorted_indices]
    cumulative_scores = np.cumsum(sorted_scores)
    normalized_cumulative_scores = cumulative_scores / cumulative_scores[-1]
    n = len(scores)
    all_coord = np.vstack((range(n), normalized_cumulative_scores)).T
    first_point = all_coord[0]
    line_vec = all_coord[-1] - all_coord[0]
    line_vec = line_vec / np.sqrt(np.sum(line_vec**2))
    vec_from_first = all_coord - first_point
    scalar_prod = np.sum(vec_from_first * np.tile(line_vec, (n, 1)), axis=1)
    vec_from_first_parallel = np.outer(scalar_prod, line_vec)
    vec_to_line = vec_from_first - vec_from_first_parallel
    dist_to_line = np.sqrt(np.sum(vec_to_line ** 2, axis=1))
    elbow_point = np.argmax(dist_to_line)
    return elbow_point + 1, sorted_indices[:elbow_point + 1]

scores = np.array([85, 92, 88, 96, 80, 78, 84, 93, 91, 87])
optimal_candidates, top_indices = find_elbow_point(scores)

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
plt.title('Elbow Method for Optimal Number of Candidates')
plt.show()
