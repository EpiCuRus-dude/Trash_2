import numpy as np
from scipy.stats import norm

scores = {
    "Candidate 1": [85, 90, 88],
    "Candidate 2": [70, 75, 72],
    "Candidate 3": [88, 90, 89, 87, 91]
}

priors = {
    candidate: {
        "mean": norm(loc=np.mean(scores_list), scale=10),
        "std_dev_range": (np.std(scores_list)/2, np.std(scores_list)*2)
    } for candidate, scores_list in scores.items()
}

lambda_value = 1
def utility(mean, std_dev):
    return mean - lambda_value * std_dev

for candidate, data in priors.items():
    mean_dist = data["mean"]
    std_dev_low, std_dev_high = data["std_dev_range"]
    std_dev_values = np.linspace(std_dev_low, std_dev_high, 100)
    expected_utility = np.mean([utility(mean_dist.mean(), std_dev) for std_dev in std_dev_values])
    print(f"Expected Utility for {candidate}: {expected_utility:.2f}")
