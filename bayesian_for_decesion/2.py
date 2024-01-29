#it may work

import numpy as np


distances = np.random.rand(M, k)  


prior = 1 / (M * k)


likelihood = 1 / distances


likelihood /= likelihood.sum(axis=1, keepdims=True)


posterior = prior * likelihood


best_match_index = np.unravel_index(np.argmax(posterior), posterior.shape)
best_match = posterior[best_match_index]

print("Best Match Index:", best_match_index)
print("Best Match Probability:", best_match)

