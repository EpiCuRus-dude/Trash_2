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


#Case 1: Using nn.BCELoss() (outputs must have sigmoid applied)
sigmoid_outputs = torch.sigmoid(outputs)  # Apply sigmoid manually
criterion_bce = nn.BCELoss()
loss_bce = criterion_bce(sigmoid_outputs, labels)  # Calculate loss with sigmoid applied
print("BCELoss:", loss_bce.item())

# Case 2: Using nn.BCEWithLogitsLoss() (applies sigmoid internally)
criterion_bce_logits = nn.BCEWithLogitsLoss()
loss_bce_logits = criterion_bce_logits(outputs, labels)  # Compute loss without sigmoid applied
print("BCEWithLogitsLoss:", loss_bce_logits.item())


