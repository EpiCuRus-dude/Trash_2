import torch
from transformers import CLIPProcessor, CLIPModel
import faiss
import numpy as np
from datasets import load_from_disk
from PIL import Image
import requests

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_name = "openai/clip-vit-large-patch14"
model = CLIPModel.from_pretrained(model_name).to(device)
processor = CLIPProcessor.from_pretrained(model_name)

dataset_path = "/path/to/imagenet_sketch"
dataset = load_from_disk(dataset_path)

def process_example(example):
    inputs = processor(images=example["image"], return_tensors="pt", padding=True)
    with torch.no_grad():
        outputs = model.get_image_features(**inputs.to(device))
    return {"embeddings": outputs.cpu().numpy()}

dataset = dataset.map(process_example, batched=True, batch_size=8)

image_embeddings = np.vstack(dataset["embeddings"])
dimension = image_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(image_embeddings)

faiss.write_index(index, "imagenet_sketch_index.faiss")

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(images=image, return_tensors="pt", padding=True).to(device)
with torch.no_grad():
    query_embedding = model.get_image_features(**inputs).cpu().numpy()

k = 5
distances, indices = index.search(query_embedding, k)

print(f"Top {k} similar images in the dataset are at indices: {indices}")

index = faiss.read_index("imagenet_sketch_index.faiss")
