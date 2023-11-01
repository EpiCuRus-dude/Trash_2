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


# Initialize the manual MLP
input_dim = 2  # Input dimension (for demonstration, we use 2D data points)
hidden_dim = 5  # Number of neurons in the hidden layer
output_dim = 3  # Output dimension (3 classes for classification)

# Initialize the neural network
manual_mlp_model = MLP(input_dim, hidden_dim, output_dim).to(device)

# Print the manual MLP model architecture
print(manual_mlp_model)

# Fetch and display the initial weights and biases
manual_mlp_initial_weights1 = manual_mlp_model.W1.data.cpu().numpy()
manual_mlp_initial_bias1 = manual_mlp_model.B1.data.cpu().numpy()
manual_mlp_initial_weights2 = manual_mlp_model.W2.data.cpu().numpy()
manual_mlp_initial_bias2 = manual_mlp_model.B2.data.cpu().numpy()

print(f"Manual MLP Initial Weights 1: {manual_mlp_initial_weights1.shape}")
print(f"Manual MLP Initial Bias 1: {manual_mlp_initial_bias1.shape}")
print(f"Manual MLP Initial Weights 2: {manual_mlp_initial_weights2.shape}")
print(f"Manual MLP Initial Bias 2: {manual_mlp_initial_bias2.shape}")


X_tensor = torch.FloatTensor(X).to(device)
y_tensor = torch.FloatTensor(y).to(device)


class MLP(nn.Module):
  def __init__(self, input_dim, hid_dim, output_dim):
    super(MLP, self).__init__()

    self.W1 = torch.Parameter(torch.randn(input_dim, hid_dim))
    self.B1 = torch.Parameter(torch.randn(hid_dim))

    self.W2 = torch.Parameter(torch.randn(hid_dim, output_dim))
    self.B2 = torch.Parameter(torch.randn(output_dim))

    self.relu = nn.ReLU()
    self.softmax = nn.Softmax(dim=1)

  def forward(self, x):
    x = torch.mm(x, self.W1) + self.B1
    x = self.relu(x)

    x = torch.mm(x, self.W2) + self.B2

    x = self.softmax(x)

    return x




