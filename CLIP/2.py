inputs = clip_processor(images=image_data, return_tensors="pt")

with torch.no_grad():
    image_embeddings = clip_model(**inputs).image_embeds 
