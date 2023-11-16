
unknown_tokens = Counter()
for text in texts:
    =
    tokenized_text = tokenizer.tokenize(text)

  
    decoded_text = tokenizer.convert_tokens_to_string(tokenized_text).split()

    
    original_words = set(text.split())
    for word in original_words:
        if word not in decoded_text:
            unknown_tokens[word] += 1



new_tokens = ["CATT", "DOGG"]
tokenizer.add_tokens(new_tokens)


model.resize_token_embeddings(len(tokenizer))


input_text = "CATT is a new word."
input_ids = tokenizer.encode(input_text, return_tensors="pt")
outputs = model.generate(input_ids)
decoded_output = tokenizer.decode(outputs[0])
