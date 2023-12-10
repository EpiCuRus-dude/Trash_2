import shap


explainer = shap.Explainer(mlp, X_train_tfidf, feature_names=vectorizer.get_feature_names())
shap_values = explainer(X_test_tfidf)


shap.summary_plot(shap_values, feature_names=vectorizer.get_feature_names())
