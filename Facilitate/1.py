import os
import numpy as np
import matplotlib.pyplot as plt

base_path = 'path/to/your/data'  
directories = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

plt.figure(figsize=(10, 6))
colors = plt.cm.jet(np.linspace(0, 1, len(directories)))

for i, dir_name in enumerate(directories):
    train_path = os.path.join(base_path, dir_name, "train.npy")
    val_path = os.path.join(base_path, dir_name, "val.npy")
    
    if os.path.exists(train_path) and os.path.exists(val_path):
        train_data = np.load(train_path)
        val_data = np.load(val_path)
        x_axis = np.arange(len(train_data))
        
        plt.plot(x_axis, train_data, label=f'train_{dir_name}', linestyle='-', color=colors[i])
        plt.plot(x_axis, val_data, label=f'val_{dir_name}', linestyle='--', color=colors[i])

plt.title("Training and Validation Data")
plt.xlabel("Data Point Index")
plt.ylabel("Value")
plt.legend()
plt.show()
