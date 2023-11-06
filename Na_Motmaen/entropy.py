import torch
import torch.nn.functional as F

# Assume we have a small vocabulary
vocab = ['<pad>', '<eos>', 'i', 'like', 'love', 'cat', 'cats', 'know']
vocab_size = len(vocab)

# Simulate probability distributions for next tokens in the sentences:
# "I like cat", "Love cat", "I know cats", ...
# For simplicity, let's say our model only predicts the next token after each word
prob_distributions = torch.tensor([
    [0.1, 0.1, 0.05, 0.5, 0.05, 0.1, 0.1, 0.0],  # After 'I', likely 'like' or 'know'
    [0.1, 0.2, 0.1, 0.4, 0.1, 0.1, 0.0, 0.0],  # After 'like', likely 'cat'
    [0.0, 0.9, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0],  # After 'cat', likely end of sentence
    [0.2, 0.1, 0.1, 0.1, 0.4, 0.1, 0.0, 0.0],  # After 'Love', likely 'cat'
    [0.1, 0.1, 0.0, 0.0, 0.0, 0.2, 0.6, 0.0],  # After 'know', likely 'cats'
    [0.0, 0.9, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0],  # Likely end of sentence after 'cats'
], dtype=torch.float)

# Calculate the entropy for the simulated probability distributions
def calculate_entropy(prob_distributions):
    # Use a small epsilon to prevent log(0)
    epsilon = 1e-5
    log_probs = torch.log(prob_distributions + epsilon)
    entropy = -torch.sum(prob_distributions * log_probs, dim=1)
    return entropy

entropies = calculate_entropy(prob_distributions)

# Output the entropy for each token position
for i, entropy in enumerate(entropies):
    print(f"Entropy for token position {i+1}: {entropy.item()}")
