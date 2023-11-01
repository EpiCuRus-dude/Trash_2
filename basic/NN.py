# Importing necessary libraries
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np


torch.manual_seed(0)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate synthetic data
X, y = make_blobs(n_samples=300, centers=3, random_state=42, cluster_std=1.0)
labels = ["Class 0", "Class 1", "Class 2"]

# Plot the synthetic data
plt.figure(figsize=(8, 6))
for label, class_name in enumerate(labels):
    plt.scatter(X[y == label][:, 0], X[y == label][:, 1], label=class_name)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.title("Synthetic Multi-Class Data")
plt.show()


