vectorizer = TfidfVectorizer()
feature_names = vectorizer.get_feature_names_out()
tfidf_query = vectorizer.transform(query)

scores = tfidf_query.toarray().flatten()
sorted_indices = scores.argsort()[::-1]  # Sort indices by score in descending order

top_n = 5
print("Top keywords in the query:")
for idx in sorted_indices[:top_n]:
    if scores[idx] > 0:  # Only consider words with a score
        print(f"{feature_names[idx]} (Score: {scores[idx]:.4f})")
