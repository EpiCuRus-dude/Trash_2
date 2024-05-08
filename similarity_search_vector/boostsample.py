import numpy as np
from scipy.stats import norm


scores = np.array([75, 82, 90, 68, 95, 84, 70, 89, 78, 91, 77, 96, 81, 85, 88, 93, 69, 87, 83, 86])


M = 5


np.random.seed(42)  
n_iterations = 1000  
selected_indices = []

for _ in range(n_iterations):
    sampled_scores = np.random.choice(scores, size=len(scores), replace=True)
    sorted_indices = np.argsort(sampled_scores)[-M:]
    selected_indices.append(sorted_indices)


frequency_of_selection = np.mean([np.bincount(indices, minlength=len(scores)) for indices in selected_indices], axis=0)


mean_score = np.mean(scores)
std_dev = np.std(scores)
confidence_intervals = [(score - 1.96 * std_dev, score + 1.96 * std_dev) for score in scores]

