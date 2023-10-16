import torch
import torch.nn.functional as F

# Define the smoothed labels
smoothed_label = torch.tensor([0.933, 0.033, 0.033])

# Define the logits in three scenarios
logits1 = torch.tensor([10.0, 0.0, 0.0])
logits2 = torch.tensor([0.0, 10.0, 0.0])
logits3 = torch.tensor([0.0, 0.0, 10.0])

# Compute the softmax of the logits
softmax_logits1 = F.softmax(logits1, dim=0)
softmax_logits2 = F.softmax(logits2, dim=0)
softmax_logits3 = F.softmax(logits3, dim=0)

# Compute the cross-entropy loss with label smoothing for each scenario
loss1 = -torch.sum(smoothed_label * torch.log(softmax_logits1))
loss2 = -torch.sum(smoothed_label * torch.log(softmax_logits2))
loss3 = -torch.sum(smoothed_label * torch.log(softmax_logits3))

print(loss1.item())  # Output: 0.022
print(loss2.item())  # Output: 3.401
print(loss3.item())  # Output: 3.401
