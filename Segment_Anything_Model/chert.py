import numpy as np
from sklearn.metrics import confusion_matrix, f1_score




conf_matrix_manual, f1_score_manual_macro = compute_metrics(all_true, all_res)
f1_score_manual_micro = compute_micro_f1(conf_matrix_manual)


conf_matrix_sklearn = confusion_matrix(all_true, all_res)
f1_score_sklearn_macro = f1_score(all_true, all_res, average='macro')
f1_score_sklearn_micro = f1_score(all_true, all_res, average='micro')


print("Confusion Matrix (Manual):")
print(conf_matrix_manual)
print("Macro F1 Score (Manual):", f1_score_manual_macro)
print("Micro F1 Score (Manual):", f1_score_manual_micro)

print("\nConfusion Matrix (sklearn):")
print(conf_matrix_sklearn)
print("Macro F1 Score (sklearn):", f1_score_sklearn_macro)
print("Micro F1 Score (sklearn):", f1_score_sklearn_micro)
