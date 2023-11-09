# Generate 10 samples of predicted probabilities for a three-class classification problem
y_prob = np.array([
    [0.7, 0.2, 0.1],  # True label: dog
    [0.2, 0.6, 0.2],  # True label: fish
    [0.4, 0.1, 0.5],  # True label: fish
    [0.1, 0.8, 0.1],  # True label: fish
    [0.3, 0.3, 0.4],  # True label: cat
    [0.6, 0.2, 0.2],  # True label: dog
    [0.2, 0.2, 0.6],  # True label: cat
    [0.5, 0.3, 0.2],  # True label: dog
    [0.1, 0.7, 0.2],  # True label: fish
    [0.3, 0.4, 0.3]   # True label: fish
])

# The true class labels corresponding to the samples
y_true = np.array([0, 1, 1, 1, 2, 0, 2, 0, 1, 1])  # 0: dog, 1: fish, 2: cat
