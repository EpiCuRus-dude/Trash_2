def modified_z_score(scores, threshold=3.5):
    median = np.median(scores)
    mad = np.median(np.abs(scores - median))
    modified_z_scores = 0.6745 * (scores - median) / mad
    return scores[np.abs(modified_z_scores) > threshold]


top_candidates = modified_z_score(scores)
