
shap_sum = np.abs(shap_values).mean(axis=0)
importance_df = pd.DataFrame([feature_names, shap_sum]).T
importance_df.columns = ['feature', 'shap_value']
importance_df.sort_values(by='shap_value', ascending=False, inplace=True)


N = 3  
important_words = importance_df.head(N)['feature'].tolist()


print("Important Words:", important_words)
