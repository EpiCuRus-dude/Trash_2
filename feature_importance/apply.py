


explainer = shap.LinearExplainer(model, X_train_vec, feature_dependence="independent")
shap_values = explainer.shap_values(X_test_vec)


shap_sum = np.abs(shap_values).mean(axis=0)
feature_names = vectorizer.get_feature_names_out()
importance_df = pd.DataFrame([feature_names, shap_sum]).T
importance_df.columns = ['feature', 'shap_value']
important_features = importance_df.sort_values(by='shap_value', ascending=False).head(5)['feature'].tolist()



augmented_texts = texts + ["text with " + " ".join(important_features)] * 10
augmented_labels = np.concatenate((labels, np.random.randint(0, 2, size=10)))

X_train_augmented = vectorizer.fit_transform(augmented_texts)
y_train_augmented = augmented_labels
model.fit(X_train_augmented, y_train_augmented)

