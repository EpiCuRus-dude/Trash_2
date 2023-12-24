from transformers import AutoTokenizer, AutoModelForCausalLM


model_name = "gpt2"  
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


text = "The quick brown fox jumps over the lazy dog."


input_ids = tokenizer.encode(text, return_tensors='pt')

# Encode the text (get model outputs)
outputs = model(input_ids)


last_hidden_states = outputs.last_hidden_state
last_hidden_states.shape  
