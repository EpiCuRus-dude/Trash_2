
priors = {f'Index_{i}': 1/num_indices for i in range(1, num_indices+1)}


likelihoods = {}
for index, distances in top_k_results.items():
    mean = np.mean(distances)
    variance = np.var(distances)
    likelihoods[index] = [norm.pdf(d, mean, np.sqrt(variance)) for d in distances]


posteriors = {}
for index in top_k_results.keys():
    posterior = [priors[index] * l for l in likelihoods[index]]
    posteriors[index] = sum(posterior)


total_posterior = sum(posteriors.values())
normalized_posteriors = {index: p / total_posterior for index, p in posteriors.items()}
best_match_index = max(normalized_posteriors, key=normalized_posteriors.get)

print("Normalized Posteriors:", normalized_posteriors)
print("Best Match Index:", best_match_index)
