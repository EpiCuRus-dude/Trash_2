from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize
import matplotlib.pyplot as plt
from itertools import cycle


true = ['cat', 'fish', 'dog', 'cat', 'cat', 'fish', 'dog']
preds = ['fish', 'fish', 'fish', 'cat', 'dog', 'dog', 'dog']


probabilities = [
    [0.1, 0.6, 0.3],  # Probability for first sample
    [0.1, 0.7, 0.2],
    [0.2, 0.5, 0.3],
    [0.7, 0.1, 0.2],
    [0.2, 0.3, 0.5],
    [0.3, 0.3, 0.4],
    [0.2, 0.4, 0.4]
]


label_mapping = {'cat': 0, 'dog': 1, 'fish': 2}
true_numerical = [label_mapping[label] for label in true]


n_classes = 3
true_binarized = label_binarize(true_numerical, classes=range(n_classes))


fpr = dict()
tpr = dict()
roc_auc = dict()

for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(true_binarized[:, i], [p[i] for p in probabilities])
    roc_auc[i] = auc(fpr[i], tpr[i])


colors = cycle(['blue', 'red', 'green'])
class_names = ['cat', 'dog', 'fish']
plt.figure(figsize=(10, 8))

for i, color in zip(range(n_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=2,
             label=f'ROC curve of class {class_names[i]} (area = {roc_auc[i]:.2f})')

plt.plot([0, 1], [0, 1], 'k--', lw=2)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Multiclass ROC')
plt.legend(loc="lower right")
plt.show()

