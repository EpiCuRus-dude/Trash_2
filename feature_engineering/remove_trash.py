import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk


nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    # Normalize text
    text = text.lower()
    
    
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    
    tokens = word_tokenize(text)
    
    
    filtered_tokens = [word for word in tokens if word not in stopwords.words('english')]
    
    return " ".join(filtered_tokens)


text = "Example string with some words like X, and also Y, maybe Z. Plus numbers 123 and special characters !@#"

cleaned_text = preprocess_text(text)
print("Cleaned text:", cleaned_text)
