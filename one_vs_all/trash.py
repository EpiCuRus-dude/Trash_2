import torch
import torch.nn as nn
https://mmuratarat.github.io/2019-10-02/multi-class-classification

criterion = nn.BCELoss()


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


loss = criterion(outputs, labels)


