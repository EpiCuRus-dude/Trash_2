import numpy as np

def topsis(scores):

    norms = np.linalg.norm(scores, axis=0)
    normalized_scores = scores / norms


    weights = np.array([0.5, -0.5])  

    
    weighted_scores = normalized_scores * weights

    
    ideal = np.max(weighted_scores, axis=0)
    negative_ideal = np.min(weighted_scores, axis=0)


    dist_ideal = np.sqrt(np.sum((weighted_scores - ideal)**2, axis=1))
    dist_negative_ideal = np.sqrt(np.sum((weighted_scores - negative_ideal)**2, axis=1))

   
    topsis_scores = dist_negative_ideal / (dist_ideal + dist_negative_ideal)


    best_candidate_index = np.argmax(topsis_scores)
    return best_candidate_index, topsis_scores[best_candidate_index]


scores = np.array([
    [4, 0.5],  # Candidate 1: mean=4, std=0.5
    [5, 0.7],  # Candidate 2: mean=5, std=0.7
    [3, 0.2]   # Candidate 3: mean=3, std=0.2
])
best_candidate, best_score = topsis(scores)
print(f"Best Candidate Index: {best_candidate}, Score: {best_score:.2f}")
