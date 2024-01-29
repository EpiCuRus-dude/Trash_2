import numpy as np
from scipy.stats import norm


np.random.seed(42)
M = 3  
N = 10  


distances_from_indices = {f'Index_{i+1}': np.random.rand(N) for i in range(M)}

means_vars = {index: (np.mean(distances), np.var(distances)) for index, distances in distances_from_indices.items()}


priors = {candidate: 1/N for candidate in range(N)}


posteriors = {}
uncertainties = {}
for candidate in range(N):
    candidate_posteriors = []
    for index in distances_from_indices:
        distance = distances_from_indices[index][candidate]
        mean, var = means_vars[index]
        likelihood = norm.pdf(distance, mean, np.sqrt(var))
        candidate_posterior = likelihood * priors[candidate]
        candidate_posteriors.append(candidate_posterior)
    total_candidate_posterior = sum(candidate_posteriors)
    posteriors[candidate] = total_candidate_posterior
    uncertainties[candidate] = np.std(candidate_posteriors)


total_posterior = sum(posteriors.values())
normalized_posteriors = {candidate: posterior / total_posterior for candidate, posterior in posteriors.items()}


best_candidates = sorted(normalized_posteriors, key=normalized_posteriors.get, reverse=True)[:5]

print("Best Candidates based on Bayesian Inference:", best_candidates)
print("Individual Uncertainties for Each Candidate:")
for candidate in best_candidates:
    print(f"Candidate {candidate}: {uncertainties[candidate]}")
