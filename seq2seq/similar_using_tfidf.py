from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def func(input_str, string_list, method='bag_of_words'):
    
    if method == 'bag_of_words':
        vectorizer = CountVectorizer().fit(string_list + [input_str])
    elif method == 'tfidf':
        vectorizer = TfidfVectorizer().fit(string_list + [input_str])
    else:
        raise ValueError("Method must be 'bag_of_words' or 'tfidf'")

   
    vectorized_strings = vectorizer.transform(string_list)
    vectorized_input = vectorizer.transform([input_str])

   
    similarities = cosine_similarity(vectorized_input, vectorized_strings).flatten()

   
    most_similar_index = np.argmax(similarities)
    return string_list[most_similar_index], similarities[most_similar_index]


