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
