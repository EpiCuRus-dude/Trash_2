import torch
import torch.nn as nn
import torch.nn.functional as F

class Smoothed_Cross_Entropy_Loss(nn.Module):
    def __init__(self, smoothing=0.1):
        super(Smoothed_Cross_Entropy_Loss, self).__init__()
        self.smoothing = smoothing

    def forward(self, logits, target):
        num_classes = logits.size(-1)
        smoothed_target = (1 - self.smoothing) * F.one_hot(target, num_classes) + self.smoothing / num_classes
        log_prob = F.log_softmax(logits, dim=-1)
        loss = -torch.sum(log_prob*smoothed_target)/logits.size(0)
        return loss


# Define the logits and correct target
logits = torch.tensor([[10000.0, 0.0, 0.0, 0.0, 0.0]])  # Logits for a single token output
target = torch.tensor([0])  # Correct token ID for "goodbye"

device = torch.device("cuda:0")

# Create the loss function
smoothed_criterion = Smoothed_Cross_Entropy_Loss(smoothing=0.1)

# Compute the Label Smoothed Cross Entropy Loss
smoothed_loss = smoothed_criterion(logits, target)
print(smoothed_loss.item())

device = torch.device("cuda:0")

# Create the loss function
smoothed_criterion = Smoothed_Cross_Entropy_Loss(smoothing=0.1).to(device)




logtist = torch.randn(64, 128, 101).to(device)
target = torch.randint(0, 101, (64, 128)).to(device)

# Compute the Label Smoothed Cross Entropy Loss
smoothed_loss = smoothed_criterion(logits, target)
print(smoothed_loss.item())
