import scipy.stats as stats

def bayesian_ranking(scores, alpha=1, beta=1):
    ranked_candidates = []
    for score in scores:
        posterior = stats.beta(alpha + score, beta + (100 - score))
        mean_posterior = posterior.mean()
        ranked_candidates.append((score, mean_posterior))
    ranked_candidates.sort(key=lambda x: x[1], reverse=True)
    return [score for score, _ in ranked_candidates]


top_candidates = bayesian_ranking(scores)
