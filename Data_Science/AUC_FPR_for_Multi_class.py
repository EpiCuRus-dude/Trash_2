from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize
import numpy as np
import matplotlib.pyplot as plt


true = np.array(['cat', 'fish', 'dog', 'cat', 'cat', 'fish', 'dog'])
pred_probs = np.array([
    [0.1, 0.6, 0.3],  # Predicted probabilities for 'fish'
    [0.2, 0.7, 0.1],  # Predicted probabilities for 'fish'
    [0.3, 0.4, 0.3],  # Predicted probabilities for 'fish'
    [0.7, 0.1, 0.2],  # Predicted probabilities for 'cat'
    [0.3, 0.3, 0.4],  # Predicted probabilities for 'dog'
    [0.2, 0.2, 0.6],  # Predicted probabilities for 'dog'
    [0.1, 0.3, 0.6],  # Predicted probabilities for 'dog'
])


classes = ['cat', 'dog', 'fish']


true_binarized = label_binarize(true, classes=classes)


fpr = dict()
tpr = dict()
roc_auc = dict()
n_classes = len(classes)

for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(true_binarized[:, i], pred_probs[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])


plt.figure(figsize=(8, 6))
colors = ['blue', 'green', 'red']
for i, color in zip(range(n_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=2,
             label='ROC curve of class {0} (area = {1:0.2f})'
             ''.format(classes[i], roc_auc[i]))

plt.plot([0, 1], [0, 1], 'k--', lw=2)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Multiclass ROC')
plt.legend(loc="lower right")
plt.show()

