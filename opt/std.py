import numpy as np

Scores = np.random.randint(50, 100, size=(1, 3, 4))  # Random data for 1 test

_, num_candidates, num_refs = Scores.shape


std_devs = []

std_devs = np.zeros(num_candidates)
avg_scores = np.zeros(num_candidates)


for candidate in range(num_candidates):
    scores = Scores[0, candidate, :]
    std_devs[candidate] = np.std(scores)
    avg_scores[candidate] = np.mean(scores)


std_devs_normalized = std_devs / np.max(std_devs)
avg_scores_normalized = avg_scores / np.max(avg_scores)
combined_scores = ... # whatever


winner_index = np.argmax(combined_scores)


candidate_names = [...]

print("Standard Deviation Analysis Winner (Named):", candidate_names[winner_index])
