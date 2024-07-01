import re
import nltk
from nltk.tokenize import sent_tokenize




def find_pirads_sentences(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    pirads_sentences = [sentence for sentence in sentences if re.search(r"\bPI[-\s]?RADS\b", sentence, re.IGNORECASE)]
    return pirads_sentences


pirads_sentences = find_pirads_sentences(text)
print("Sentences containing 'dddd':")
for sentence in pirads_sentences:
    print(sentence)

def extract_sentences_with_words(text, word1, word2):
    sentences = sent_tokenize(text)
    word_pattern = rf"(?=.*\b{re.escape(word1)}\b)(?=.*\b{re.escape(word2)}\b).*"
    filtered_sentences = [sentence for sentence in sentences if re.search(word_pattern, sentence, re.IGNORECASE)]
    return filtered_sentences

def extract_sentences_with_and_without_words(text, word1, word2):
    sentences = sent_tokenize(text)

    word_pattern = rf"\b{re.escape(word1)}\b(?!.*\b{re.escape(word2)}\b)"
    filtered_sentences = [sentence for sentence in sentences if re.search(word_pattern, sentence, re.IGNORECASE)]
    return filtered_sentences

def extract_sentences_with_any_words(text, words):
    sentences = sent_tokenize(text)
   
    word_pattern = rf"\b(?:{'|'.join(re.escape(word) for word in words)})\b"
    filtered_sentences = [sentence for sentence in sentences if re.search(word_pattern, sentence, re.IGNORECASE)]
    return filtered_sentences



def extract_sentences_with_all_words(text, words):
    sentences = sent_tokenize(text)

    word_pattern = rf"(?=.*\b{re.escape(words[0])}\b)"
    for word in words[1:]:
        word_pattern += rf"(?=.*\b{re.escape(word)}\b)"
    word_pattern += r".*"
    
    filtered_sentences = [sentence for sentence in sentences if re.search(word_pattern, sentence, re.IGNORECASE)]
    return filtered_sentences



