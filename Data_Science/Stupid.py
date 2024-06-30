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
