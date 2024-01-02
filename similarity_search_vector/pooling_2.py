from transformers import GPT2Tokenizer, GPT2Model
import torch


tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')


titles = ["Title 1", "Title 2", "...", "Title 500"]


inputs = tokenizer(titles, padding='max_length', truncation=True, max_length=512, return_tensors="pt")


with torch.no_grad():
    outputs = model(**inputs)
    hidden_states = outputs.last_hidden_state


attention_mask = inputs['attention_mask'].unsqueeze(-1)
sum_hidden_states = torch.sum(hidden_states * attention_mask, dim=1)
sum_mask = torch.clamp(attention_mask.sum(dim=1), min=1e-9)
mean_pooled = sum_hidden_states / sum_mask


