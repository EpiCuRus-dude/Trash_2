from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
X = vectorizer.fit_transform(df['description']).toarray()


def get_top_keywords(tfidf_vector, feature_names, top_n=5):
    sorted_nzs = np.argsort(tfidf_vector)[:-top_n-1:-1]
    return [feature_names[i] for i in sorted_nzs]

feature_names = vectorizer.get_feature_names_out()
df['keywords'] = [get_top_keywords(tfidf_vector, feature_names) for tfidf_vector in X]

print(df[['description', 'keywords']])
