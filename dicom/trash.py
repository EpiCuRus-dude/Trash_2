def load_dicom_image(file_path):
    dicom = pydicom.dcmread(file_path)
    image = dicom.pixel_array
    image = image - np.min(image)  # Normalize to 0-1
    image = (image / np.max(image) * 255).astype(np.uint8)  # Normalize to 0-255 and convert to uint8
        
    if len(image.shape) == 2:
        image = np.stack((image,) * 3, axis=-1)
    return Image.fromarray(image)

def plot_image(image, title="Image"):
    plt.imshow(image)
    plt.title(title)
    plt.axis("off")
    plt.show()

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
