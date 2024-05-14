import numpy as np



def evaluate_threshold(threshold, scores):
    selected_candidates = scores[scores >= threshold]
    # Example criterion: maximizing the number of candidates
    return len(selected_candidates)

def grid_search_threshold(scores, num_points=100):
    thresholds = np.linspace(np.min(scores), np.max(scores), num_points)
    best_threshold = thresholds[0]
    best_value = 0
    
    for threshold in thresholds:
        value = evaluate_threshold(threshold, scores)
        if value > best_value:
            best_value = value
            best_threshold = threshold
    
    return scores[scores >= best_threshold]


top_candidates = grid_search_threshold(scores)
top_candidates
