import numpy as np

Scores = np.random.randint(50, 100, size=(10, 3, 4))

num_tests, num_candidates, num_refs = Scores.shape

winners = []

for test in range(num_tests):
    borda_points = np.zeros(num_candidates)
    for ref in range(num_refs):
        scores = Scores[test, :, ref]
        ranks = np.argsort(scores)[::-1]
        for i, candidate in enumerate(ranks):
            borda_points[candidate] += (num_candidates - i)
    winner_index = np.argmax(borda_points)
    winners.append(winner_index)

print("Winners for Each Test (Indices):", winners)

candidate_names = [...]

winners_named = [candidate_names[winner] for winner in winners]

print("Winners for Each Test (Named):", winners_named)
