def pareto_principle(scores):
    sorted_scores = np.sort(scores)[::-1]
    cumulative_scores = np.cumsum(sorted_scores)
    total_score = cumulative_scores[-1]
    threshold_index = np.searchsorted(cumulative_scores, 0.8 * total_score)
    return sorted_scores[:threshold_index + 1]


top_candidates = pareto_principle(scores)
