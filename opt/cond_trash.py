import numpy as np

weights = np.array([1, 1, 1, 2])

Scores = np.random.randint(50, 100, size=(50, 3, 4))

num_tests, num_candidates, num_refs = Scores.shape

pairwise_wins = np.zeros((num_candidates, num_candidates))

for test in range(num_tests):
    for ref in range(num_refs):
        scores = Scores[test, :, ref]
        weighted_scores = scores * weights[ref]
        for i in range(num_candidates):
            for j in range(num_candidates):
                if i != j:
                    if weighted_scores[i] > weighted_scores[j]:
                        pairwise_wins[i, j] += 1

condorcet_winner = None
for i in range(num_candidates):
    if all(pairwise_wins[i, j] > pairwise_wins[j, i] for j in range(num_candidates) if i != j):
        condorcet_winner = i
        break

print("Pairwise Wins Matrix:")
print(pairwise_wins)

if condorcet_winner is not None:
    print("Condorcet Winner (Index):", condorcet_winner)
else:
    print("No Condorcet Winner")
