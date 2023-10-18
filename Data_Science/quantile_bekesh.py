# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a sample DataFrame with 10 labels and random frequencies
np.random.seed(0)
labels = [f'Label_{i}' for i in range(1, 11)]
data = {'A': np.random.choice(labels, 1000)}
df = pd.DataFrame(data)



label_frequncies  = df['A'].value_counts(normalize=True).sort_values(ascending=False)

q90 = label_frequncies.quantile(0.9)
q50 = label_frequncies.quantile(0.5)

plt.figure(figsize=(16,9))

# Bar plot
label_frequncies.plot(kind='bar')

# Add red dashed lines for the 90th and 50th quantiles
plt.axhline(y=q90, color='r', linestyle='--', label=f'90th Quantile: {q90:.4f}')
plt.axhline(y=q50, color='r', linestyle='-.', label=f'50th Quantile: {q50:.4f}')


# Annotations with arrows
plt.annotate(f'90th Quantile', 
             xy=(len(label_frequncies)/2, q90), 
             xytext=(len(label_frequncies)/2, q90 + 0.005),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, 
             horizontalalignment='center')

plt.annotate(f'New 50th Quantile', 
             xy=(len(label_frequncies)/2, q50), 
             xytext=(len(label_frequncies)/2, q50 + 0.005),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, 
             horizontalalignment='center')

