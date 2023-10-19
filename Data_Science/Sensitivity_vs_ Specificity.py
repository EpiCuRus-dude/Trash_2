import pandas as pd
#### NEEDS SOME WORK
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


#### imbalanced dtataset example

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Generate synthetic data for a three-class problem (imbalanced)
np.random.seed(0)
num_samples = 1000
true_labels = np.random.choice([0, 1, 2], num_samples, p=[0.8, 0.1, 0.1])
predicted_scores = np.random.rand(num_samples, 3)  # Random scores for each class

# Create a DataFrame
data = {'True Class': true_labels}
for i in range(3):
    data[f'Predicted Score Class {i}'] = predicted_scores[:, i]

df = pd.DataFrame(data)

# Define a function to calculate sensitivity and specificity for a given threshold
def calculate_metrics(df, threshold, class_label):
    predicted_class = (df[f'Predicted Score Class {class_label}'] >= threshold).astype(int)
    true_positive = ((df['True Class'] == class_label) & (predicted_class == 1)).sum()
    false_positive = ((df['True Class'] != class_label) & (predicted_class == 1)).sum()
    true_negative = ((df['True Class'] != class_label) & (predicted_class == 0)).sum()
    false_negative = ((df['True Class'] == class_label) & (predicted_class == 0)).sum()
    
    sensitivity = true_positive / (true_positive + false_negative)
    specificity = true_negative / (true_negative + false_positive)
    
    return sensitivity, specificity

# Define a range of thresholds
thresholds = np.linspace(0, 1, 100)

# Calculate sensitivity and specificity for each threshold for a specific class (e.g., Class 0)
class_label_to_plot = 0
sensitivities = []
specificities = []

for threshold in thresholds:
    sensitivity, specificity = calculate_metrics(df, threshold, class_label_to_plot)
    sensitivities.append(sensitivity)
    specificities.append(specificity)

# Plot sensitivity and specificity vs. threshold
plt.figure(figsize=(10, 6))
plt.plot(thresholds, sensitivities, label=f'Sensitivity (Class {class_label_to_plot})')
plt.plot(thresholds, specificities, label=f'Specificity (Class {class_label_to_plot})')
plt.xlabel('Threshold')
plt.ylabel('Metric Value')
plt.title('Sensitivity and Specificity vs. Threshold')
plt.legend()
plt.grid()
plt.show()

