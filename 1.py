import pandas as pd

df_tfidf = pd.DataFrame(X_tfidf.toarray(), columns=vectorizer.get_feature_names_out())
print(df_tfidf)


# Get the positions of the non-zero elements
non_zero_positions = X_tfidf.nonzero()

# Get the values of the non-zero elements
non_zero_values = X_tfidf.data

# Get the feature names
feature_names = vectorizer.get_feature_names_out()

# Print the non-zero elements and their values
for row, col, value in zip(*non_zero_positions, non_zero_values):
    print(f'Document {row}, Feature "{feature_names[col]}", TF-IDF Value: {value}')
