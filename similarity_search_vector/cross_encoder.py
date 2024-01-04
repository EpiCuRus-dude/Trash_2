##




model_name = ...
tokenizer = ..
model = AutoModelForSequenceClassification...

def rank_sentences(query, sentences):
    
    pairs = [[query, sentence] for sentence in sentences]
    encoded_input = tokenizer(pairs, padding=True, truncation=True, return_tensors='pt')

    
    with torch.no_grad():
        scores = model(**encoded_input).logits[:,1]

    
    scored_sentences = zip(sentences, scores.numpy())
    ranked_sentences = sorted(scored_sentences, key=lambda x: x[1], reverse=True)

    return ranked_sentences


query = "Your example query here"
sentences = [
    "Sentence 1 related to the query",
    "Sentence 2 not so related",
    "Sentence 3 very relevant to the query"
]

ranked = rank_sentences(query, sentences)
for sentence, score in ranked:
    print(f"Score: {score:.4f} - Sentence: {sentence}")

