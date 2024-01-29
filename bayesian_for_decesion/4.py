import numpy as np
from scipy.stats import norm


np.random.seed(42)
M = 3  
N = 10  

distances_from_indices = {f'Index_{i+1}': np.random.rand(N) for i in range(M)}

means_vars = {index: (np.mean(distances), np.var(distances)) for index, distances in distances_from_indices.items()}

priors = {candidate: 1/N for candidate in range(N)}


posteriors = {}
for candidate in range(N):
    candidate_posterior = priors[candidate]
    for index in distances_from_indices:
        distance = distances_from_indices[index][candidate]
        mean, var = means_vars[index]
        likelihood = norm.pdf(distance, mean, np.sqrt(var))
        candidate_posterior *= likelihood
    posteriors[candidate] = candidate_posterior


total_posterior = sum(posteriors.values())
normalized_posteriors = {candidate: posterior / total_posterior for candidate, posterior in posteriors.items()}


posterior_values = list(normalized_posteriors.values())
uncertainty = np.std(posterior_values)


best_candidates = sorted(normalized_posteriors, key=normalized_posteriors.get, reverse=True)

print("Best Candidates based on Bayesian Inference:", best_candidates[:5])  # Top 5 candidates
print("Uncertainty (Standard Deviation of Posterior Probabilities):", uncertainty)
