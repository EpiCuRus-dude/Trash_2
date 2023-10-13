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

    
    
