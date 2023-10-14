from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import torch


class get_similarity():
  def __init__(self, initial_value=None):
    self.value = initial_value


  def get_embed(self, text):
    tokens = tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors="pt")
    with torch.no_grad():
      outputs = model(**tokens)
    return outputs

  def __call__(self, text, labels):
    
    print(text)
    print(labels)

    scores = [cosine_similarity(self.get_embed(text).numpy(), self.get_embed(label).numpy()) for label in labels] 

    most_similar_idx = np.argmax(scores)

    return scores[most_similar_idx], scores  



from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import torch


class get_similarity():
  def __init__(self, initial_value=None):
    self.value = initial_value


  def get_embed(self, text):
    tokens = tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors="pt")
    with torch.no_grad():
      outputs = model(**tokens)
    return outputs

  def __call__(self, text, labels):
    
    print(text)
    print(labels)

    scores = [cosine_similarity(self.get_embed(text).numpy(), self.get_embed(label).numpy()) for label in labels] 

    most_similar_idx = np.argmax(scores)

    return scores[most_similar_idx], scores  

    
    


from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import torch


class get_similarity():
  def __init__(self, initial_value=None):
    self.value = initial_value


  def get_embed(self, text):
    tokens = tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors="pt")
    with torch.no_grad():
      outputs = model(**tokens)
    return outputs

  def __call__(self, text, labels):
    
    print(text)
    print(labels)

    scores = [cosine_similarity(self.get_embed(text).numpy(), self.get_embed(label).numpy()) for label in labels] 

    most_similar_idx = np.argmax(scores)

    return scores[most_similar_idx], scores  

    
    
    
    


from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import torch


class get_similarity():
  def __init__(self, initial_value=None):
    self.value = initial_value


  def get_embed(self, text):
    tokens = tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors="pt")
    with torch.no_grad():
      outputs = model(**tokens)
    return outputs

  def __call__(self, text, labels):
    
    print(text)
    print(labels)

    scores = [cosine_similarity(self.get_embed(text).numpy(), self.get_embed(label).numpy()) for label in labels] 

    most_similar_idx = np.argmax(scores)

    return scores[most_similar_idx], scores  

    
    import torch
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoTokenizer, PegasusForConditionalGeneration

# Load model and tokenizer
model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")
tokenizer = AutoTokenizer.from_pretrained("google/pegasus-xsum")


labels = ["power outage", "some high wind", "low high wind", "dry good conditions", "customer impact", "scheduled blackout"]
summary_text = "high good winds"
# Tokenize text and labels
inputs_summary = tokenizer(summary_text, return_tensors="pt", padding=True, truncation=True)
inputs_labels = tokenizer(labels, return_tensors="pt", padding=True, truncation=True)

# Obtain embeddings (using mean pooling of last layer representations)
with torch.no_grad():
    outputs_summary = model.model.encoder(inputs_summary["input_ids"])
    outputs_labels = model.model.encoder(inputs_labels["input_ids"])

# Average the embeddings across the sequence length dimension to get a single vector per text/label
# Average the embeddings across the sequence length dimension to get a single vector per text/label
embeddings_summary = outputs_summary.last_hidden_state.mean(dim=1)
embeddings_labels = outputs_labels.last_hidden_state.mean(dim=1)


# Compute cosine similarity
cos_sim = cosine_similarity(embeddings_summary, embeddings_labels)

# Print or use the similarity scores
print(cos_sim[0])
