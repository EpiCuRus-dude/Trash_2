from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from nltk.tokenize import sent_tokenize


texts = [
    "A sunset over the ocean with a clear sky and calm waves. The ocean was calm under the sunset.",
    "Palm trees on a tropical beach with white sand and blue water. The beach was serene with beautiful palms.",
    "Mountain landscape with snow peaks and a clear blue sky. The peaks were covered in snow.",
    "A city skyline at night with illuminated buildings under a starry sky. The buildings shone brightly at night."
]


vectorizer = TfidfVectorizer(stop_words='english')


tfidf_matrix = vectorizer.fit_transform(texts)


feature_names = vectorizer.get_feature_names_out()


top_n = 3
sorted_indices = np.argsort(tfidf_matrix.toarray(), axis=1)[:, -top_n:]
top_keywords = [[feature_names[idx] for idx in row_indices] for row_indices in sorted_indices]


keyword_sentences = []
for text, keywords in zip(texts, top_keywords):
    sentences = sent_tokenize(text)
    sentences_with_keywords = {keyword: [] for keyword in keywords}
    for sentence in sentences:
        for keyword in keywords:
            if keyword in sentence.lower():  # Check if keyword is in the sentence
                sentences_with_keywords[keyword].append(sentence)
    keyword_sentences.append(sentences_with_keywords)


for i, keyword_sentence in enumerate(keyword_sentences):
    print(f"Text {i+1} Keyword Sentences:")
    for keyword, sentences in keyword_sentence.items():
        print(f"{keyword}: {sentences}")
    print("\n")
