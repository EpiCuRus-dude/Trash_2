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


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import nltk
from nltk.corpus import stopwords
import re



nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()  # Lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = ' '.join([word for word in text.split() if word not in stop_words])  # Remove stopwords
    return text

df['description'] = df['description'].apply(preprocess_text)

vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
X = vectorizer.fit_transform(df['description']).toarray()


def get_top_keywords(tfidf_vector, feature_names, top_n=5):
    sorted_nzs = np.argsort(tfidf_vector)[:-top_n-1:-1]
    return [feature_names[i] for i in sorted_nzs]

all_keywords = [keyword for sublist in df['keywords'] for keyword in sublist]
unique_labels = sorted(set(all_keywords))

print("Sorted unique labels:", unique_labels)

# Create one-hot encoded labels
def generate_one_hot_labels(keywords, unique_labels):
    return [1 if label in keywords else 0 for label in unique_labels]

df['one_hot_labels'] = df['keywords'].apply(lambda x: generate_one_hot_labels(x, unique_labels))
print(df[['description', 'one_hot_labels']])

