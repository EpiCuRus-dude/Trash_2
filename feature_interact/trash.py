char_vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(2, 3))
char_features = char_vectorizer.fit_transform(df['Text']).toarray()


word_vectorizer = TfidfVectorizer(analyzer='word')
word_features = word_vectorizer.fit_transform(df['Text']).toarray()


def pos_features(text):
    tokens = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)
    pos_counts = np.array([tags.count('NN') + tags.count('NNS') for word, tags in pos_tags])  # Count of nouns
    return pos_counts

pos_features = np.array([pos_features(text) for text in df['Text']])

scaler = StandardScaler()
all_features_scaled = scaler.fit_transform(all_features)




