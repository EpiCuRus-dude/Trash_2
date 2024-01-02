import torch
from transformers import GPT2Model, GPT2Tokenizer

def max_pooling(token_embeddings, attention_mask):
   
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    token_embeddings[input_mask_expanded == 0] = -1e9  # Set padding tokens to large negative value
    max_pooled = torch.max(token_embeddings, 1)[0]
    return max_pooled


tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')


inputs = tokenizer("Example text", padding=True, return_tensors="pt", max_length=512, truncation=True)


with torch.no_grad():
    outputs = model(**inputs)
    token_embeddings = outputs.last_hidden_state


attention_mask = inputs['attention_mask']
sentence_embedding = max_pooling(token_embeddings, attention_mask)

print(sentence_embedding.shape)  
