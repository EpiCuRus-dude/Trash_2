import numpy as np


scores = {
    "Candidate 1": [85, 90, 88],
    "Candidate 2": [70, 75, 72],
    "Candidate 3": [88, 90, 89, 87, 91]
}


def calculate_loss(lambda_value):
    combined_scores = []
    for scores_list in scores.values():
        mean_score = np.mean(scores_list)
        std_dev = np.std(scores_list)
        combined_score = mean_score - lambda_value * std_dev
        combined_scores.append(combined_score)

    return -np.mean(combined_scores)


lambda_values = np.linspace(0, 2, 100)  # Testing 100 lambda values from 0 to 2
losses = [calculate_loss(l) for l in lambda_values]


optimal_lambda = lambda_values[np.argmin(losses)]
optimal_loss = min(losses)


print(f"Optimal Lambda: {optimal_lambda:.2f}")
print(f"Optimal Loss: {optimal_loss:.2f}")
