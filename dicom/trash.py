def load_dicom_image(file_path):
    dicom = pydicom.dcmread(file_path)
    image = dicom.pixel_array
\
    if len(image.shape) == 2:
        image = np.stack((image,) * 3, axis=-1)
    return Image.fromarray(image)


dicom_files = ...

images = [load_dicom_image(file) for file in dicom_files]
def process_images(images):
    embeddings = []
    for image in images:
        inputs = processor(images=image, return_tensors="pt", padding=True).to(device)
        with torch.no_grad():
            outputs = model.get_image_features(**inputs)
        embeddings.append(outputs.cpu().numpy())
    return np.vstack(embeddings).astype(np.float32)

image_embeddings = process_images(images)
