# Sample N instances from each class for the test set
test_df = pd.DataFrame()
for class_label in df['A'].unique():
    class_sample = df[df['A'] == class_label].sample(n=N, random_state=42)
    test_df = pd.concat([test_df, class_sample], axis=0)
