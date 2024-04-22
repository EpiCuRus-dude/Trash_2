import numpy as np

weights = np.array([1, 1, 1, 2])

Scores = np.random.randint(50, 100, size=(50, 3, 4))

num_tests, num_candidates, num_refs = Scores.shape

pairwise_wins = np.zeros((num_candidates, num_candidates))
weighted_scores = np.zeros((num_candidates, num_refs))
for ref in range(num_refs):
    weighted_scores[:, ref] = Scores[0, :, ref] * weights[ref]

for i in range(num_candidates):
    for j in range(num_candidates):
        if i != j:
            if np.sum(weighted_scores[i]) > np.sum(weighted_scores[j]):
                pairwise_wins[i, j] += 1

condorcet_winner = None
for i in range(num_candidates):
    if all(pairwise_wins[i, j] > pairwise_wins[j, i] for j in range(num_candidates) if i != j):
        condorcet_winner = i
        break
