import numpy as np
import matplotlib.pyplot as plt



def calculate_tpr_fpr_auc(true_labels, predicted_probs, class_index):
    
    sorted_indices = np.argsort(predicted_probs[:, class_index])[::-1]
    sorted_probs = predicted_probs[sorted_indices, class_index]
    sorted_true = true_labels[sorted_indices, class_index]

    
    tpr = []
    fpr = []
    thresholds = np.unique(sorted_probs)
    for threshold in thresholds:
        
        predicted_positives = (sorted_probs >= threshold).astype(int)
        predicted_negatives = 1 - predicted_positives

        
        true_positives = (predicted_positives * sorted_true).sum()
        true_negatives = (predicted_negatives * (1 - sorted_true)).sum()

        
        false_positives = (predicted_positives * (1 - sorted_true)).sum()
        false_negatives = (predicted_negatives * sorted_true).sum()

        
        tpr.append(true_positives / (true_positives + false_negatives))
        fpr.append(false_positives / (false_positives + true_negatives))

    
    auc = np.trapz(tpr, fpr)

    return fpr, tpr, auc, thresholds



true = np.array(['cat', 'fish', 'dog', 'cat', 'cat', 'fish', 'dog'])
preds = np.array(['fish', 'fish', 'fish', 'cat', 'dog', 'dog', 'dog'])
class_names = ['cat', 'dog', 'fish']


label_mapping = {'cat': 0, 'dog': 1, 'fish': 2}
true_numerical = np.array([label_mapping[label] for label in true])

# Binarize the labels
n_classes = 3
true_binarized = label_binarize(true_numerical, classes=range(n_classes))

# Hypothetical predicted probabilities
probabilities = np.array([
    [0.1, 0.6, 0.3],  # Probability for first sample
    [0.1, 0.7, 0.2],
    [0.2, 0.5, 0.3],
    [0.7, 0.1, 0.2],
    [0.2, 0.3, 0.5],
    [0.3, 0.3, 0.4],
    [0.2, 0.4, 0.4]
])

# Calculate TPR, FPR, and AUC for each class
fpr = dict()
tpr = dict()
roc_auc = dict()
thresholds = dict()

for i in range(n_classes):
    fpr[i], tpr[i], roc_auc[i], thresholds[i] = calculate_tpr_fpr_auc(true_binarized, probabilities, i)

# Plotting the ROC curves
colors = cycle(['blue', 'red', 'green'])
plt.figure(figsize=(10, 8))

for i, color in zip(range(n_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=2,
             label=f'ROC curve of class {class_names[i]} (area = {roc_auc[i]:.2f})')

plt.plot([0, 1], [0, 1], 'k--', lw=2)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Multiclass ROC (Manual Calculation)')
plt.legend(loc="lower right")
plt.show()

