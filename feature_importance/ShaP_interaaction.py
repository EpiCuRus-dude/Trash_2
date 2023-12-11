
shap_interaction_values = explainer.shap_interaction_values(X_test)
shap.summary_plot(shap_interaction_values, X_test, feature_names=vectorizer.get_feature_names())


shap.dependence_plot(feature_idx, shap_interaction_values, X_test)


import numpy as np

# Assuming predictions and true labels are available
misclassified_indices = np.where(predictions != y_test)[0]

for idx in misclassified_indices:
    predicted_class = predictions[idx]
    true_class = y_test[idx]

    
    shap_values_pred_class = explainer.shap_values(X_test[idx])[predicted_class]
    
   
    shap_values_true_class = explainer.shap_values(X_test[idx])[true_class]

    print(f"Sample {idx} - Predicted Class: {predicted_class}, True Class: {true_class}")
    print("Top Features leading to Prediction:")
   
    for feature, value in sorted(zip(vectorizer.get_feature_names(), shap_values_pred_class), key=lambda x: -abs(x[1])):
        print(f"{feature}: {value}")

    print("\nTop Features that would have favored True Class:")
    
    for feature, value in sorted(zip(vectorizer.get_feature_names(), shap_values_true_class), key=lambda x: -abs(x[1])):
        print(f"{feature}: {value}")

    print("\n---\n")

