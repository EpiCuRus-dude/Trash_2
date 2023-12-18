from sklearn.metrics import classification_report, roc_curve, auc
from sklearn.preprocessing import label_binarize
import numpy as np


true = np.array(['cat', 'fish', 'dog', 'cat', 'cat', 'fish', 'dog'])
preds = np.array(['fish', 'fish', 'fish', 'cat', 'dog', 'dog', 'dog'])


classes = ['cat', 'dog', 'fish']


report = classification_report(true, preds, target_names=classes)
print("Classification Report:\n", report)


true_binarized = label_binarize(true, classes=classes)
preds_binarized = label_binarize(preds, classes=classes)


fpr = dict()
tpr = dict()
roc_auc = dict()
n_classes = len(classes)

for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(true_binarized[:, i], preds_binarized[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])


for i in range(n_classes):
    print(f"Class: {classes[i]}")
    print(f"  True Positive Rate (TPR): {tpr[i]}")
    print(f"  False Positive Rate (FPR): {fpr[i]}")
    print(f"  Area Under the Curve (AUC): {roc_auc[i]}\n")

