import numpy as np

Scores = np.random.randint(50, 100, size=(1, 3, 4))  # Random data for 1 test

_, num_candidates, num_refs = Scores.shape


std_devs = []

for candidate in range(num_candidates):
    scores = Scores[0, candidate, :]  =
    std_dev = np.std(scores)  
    std_devs.append(std_dev)

# Index of the candidate with the lowest standard deviation

print("Standard Deviations for Each Candidate:", std_devs)
print("Standard Deviation Analysis Winner (Index):", winner_index)


candidate_names = [...]

print("Standard Deviation Analysis Winner (Named):", candidate_names[winner_index])
