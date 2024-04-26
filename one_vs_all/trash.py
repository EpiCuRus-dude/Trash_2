import torch
import torch.nn as nn
https://mmuratarat.github.io/2019-10-02/multi-class-classification




outputs = torch.tensor([
    [0.8, 0.1, 0.3],  
    [0.7, 0.2, 0.4],  
    [0.9, 0.1, 0.2],  
])


labels = torch.tensor([
    [1, 0, 0],  
    [0, 1, 0],  
    [1, 0, 0],  
], dtype=torch.float)
import torch
import torch.nn as nn

# Example data
num_labels = 3
num_samples = 10
predictions = torch.rand(num_samples, num_labels)  # Example predictions
labels = torch.randint(0, 2, (num_samples, num_labels)).float()  # Example ground truth labels

# Define the BCEWithLogitsLoss criterion
criterion = nn.BCEWithLogitsLoss()

# Calculate the loss
loss = criterion(predictions, labels)

print("BCEWithLogitsLoss:", loss.item())

print("BCEWithLogitsLoss:", loss_bce_logits.item())


