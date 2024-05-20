import numpy as np

# Assuming scores is an NxM array where N is the number of candidates and M is the number of referees
scores = np.array([...])  # Replace with actual scores

# Calculate mean and variance for each candidate
means = np.mean(scores, axis=1)
variances = np.var(scores, axis=1)

# Calculate Signal-to-Noise Ratio (SNR) for each candidate
snr = means / np.sqrt(variances)

# Calculate Entropy for each candidate
def calculate_entropy(scores):
    probabilities = scores / np.sum(scores)
    entropy = -np.sum(probabilities * np.log2(probabilities + 1e-9))  # Adding small value to avoid log(0)
    return entropy

entropies = np.array([calculate_entropy(candidate_scores) for candidate_scores in scores])

# Threshold values for SNR and entropy based on domain knowledge or empirical analysis
snr_threshold = np.median(snr)  # Example threshold
entropy_threshold = np.median(entropies)  # Example threshold

# Decision rule
use_inverse_variance = (snr < snr_threshold) & (entropies > entropy_threshold)

# Applying the decision
if np.any(use_inverse_variance):
    weights = 1 / variances
else:
    weights = variances

# Normalize weights
weights /= np.sum(weights)

# Weighted average score for each candidate
weighted_scores = np.sum(scores * weights[:, np.newaxis], axis=1)
chosen_candidate_index = np.argmax(weighted_scores)
chosen_candidate = candidates[chosen_candidate_index]

print(f"Chosen Candidate: {chosen_candidate}")
