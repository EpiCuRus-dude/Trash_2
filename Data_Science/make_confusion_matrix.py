import numpy as np

# Assume y_true and y_pred are your data
y_true = [1, 0, 2, 2, 0, 1, 1, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2, 1, 0, 2, 1]

def create_confusion_matrix(y_true, y_pred):
    # Get the unique class labels and the number of classes
    classes = np.unique(np.concatenate((y_true, y_pred)))
    n_classes = len(classes)
    
    # Initialize the confusion matrix
    confusion_matrix = np.zeros((n_classes, n_classes), dtype=int)
    
    # Populate the confusion matrix
    for t, p in zip(y_true, y_pred):
        confusion_matrix[t, p] += 1
    
    return confusion_matrix

# Get the confusion matrix
conf_matrix = create_confusion_matrix(y_true, y_pred)
print(conf_matrix)
