import numpy as np


scores = [
    [0.9, 0.1, 0.3, 0.7, 0.4],  
    [0.8, 0.2, 0.4, 0.6, 0.5],  
    [0.85, 0.15, 0.35, 0.65, 0.45]  
]

def normalize_scores(scores):

    scores = np.array(scores)
    mean = scores.mean(axis=1, keepdims=True)
    std = scores.std(axis=1, keepdims=True)
    normalized_scores = (scores - mean) / std
    return normalized_scores

def calculate_consensus_and_conflict(scores):
   
    std_devs = np.std(scores, axis=0)
    ranges = np.ptp(scores, axis=0)
    return 1 - std_devs, 1 - ranges  # Higher values are better for both

def aggregate_scores(consensus, conflict, w1=0.5, w2=0.5):

    final_scores = w1 * consensus + w2 * conflict
    return final_scores

def select_best_candidate(final_scores):

    best_candidate_index = np.argmax(final_scores)
    return best_candidate_index


normalized_scores = normalize_scores(scores)
consensus, conflict = calculate_consensus_and_conflict(normalized_scores)
final_scores = aggregate_scores(consensus, conflict, w1=0.7, w2=0.3)
best_candidate = select_best_candidate(final_scores)

print("Best Candidate Index:", best_candidate)
print("Final Scores:", final_scores)
