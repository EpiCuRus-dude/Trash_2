import pandas as pd

# Sample data
data = {'True Class': [1, 0, 2, 1, 1, 0, 2, 0, 2, 2],
        'Predicted Class': [1, 0, 1, 2, 1, 0, 2, 1, 2, 0]}
df = pd.DataFrame(data)

# Calculate sensitivity for each class
def sensitivity(true_class, predicted_class, target_class):
    true_positive = ((true_class == target_class) & (predicted_class == target_class)).sum()
    actual_positive = (true_class == target_class).sum()
    return true_positive / actual_positive

class_labels = [0, 1, 2]
for label in class_labels:
    sens = sensitivity(df['True Class'], df['Predicted Class'], label)
    print(f'Sensitivity for Class {label}: {sens:.2f}')

# Calculate specificity for each class
def specificity(true_class, predicted_class, target_class):
    true_negative = ((true_class != target_class) & (predicted_class != target_class)).sum()
    actual_negative = (true_class != target_class).sum()
    return true_negative / actual_negative

for label in class_labels:
    spec = specificity(df['True Class'], df['Predicted Class'], label)
    print(f'Specificity for Class {label}: {spec:.2f}')


#Example II
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Generate some example data for a three-class problem
np.random.seed(0)
true_labels = np.random.randint(0, 3, 100)
predicted_scores = np.random.rand(100, 3)  # Simulated predicted scores (probabilities)

# Create an array of different thresholds
thresholds = np.linspace(0, 1, 101)

# Initialize lists to store sensitivity and specificity values
sensitivity_list = []
specificity_list = []

# Calculate sensitivity and specificity for each threshold
for threshold in thresholds:
    predicted_labels = (predicted_scores >= threshold).argmax(axis=1)  # Thresholding
    cm = confusion_matrix(true_labels, predicted_labels)
    
    # Sensitivity (True Positive Rate)
    sensitivity = cm[1, 1] / (cm[1, 1] + cm[1, 0])
    sensitivity_list.append(sensitivity)
    
    # Specificity (True Negative Rate)
    specificity = cm[0, 0] / (cm[0, 0] + cm[0, 1] + cm[0, 2] + cm[2, 0] + cm[2, 1] + cm[2, 2])
    specificity_list.append(specificity)

# Plot sensitivity and specificity vs. threshold
plt.figure(figsize=(10, 5))
plt.plot(thresholds, sensitivity_list, label='Sensitivity (True Positive Rate)')
plt.plot(thresholds, specificity_list, label='Specificity (True Negative Rate)')
plt.xlabel('Threshold')
plt.ylabel('Score')
plt.title('Sensitivity and Specificity vs. Threshold for a Three-Class Problem')
plt.legend()
plt.grid(True)
plt.show()
