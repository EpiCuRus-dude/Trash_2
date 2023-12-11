
shap_interaction_values = explainer.shap_interaction_values(X_test)
shap.summary_plot(shap_interaction_values, X_test, feature_names=vectorizer.get_feature_names())


shap.dependence_plot(feature_idx, shap_interaction_values, X_test)
