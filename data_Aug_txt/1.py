nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')







words = sentence.split()
    for _ in range(n):
        random_word = random.choice(words)
        sentence = sentence.replace(random_word, "<mask>", 1)
