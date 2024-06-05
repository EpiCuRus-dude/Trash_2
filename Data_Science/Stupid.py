
def load_dicom_series(dicom_folder):
    images = []
    for filename in sorted(os.listdir(dicom_folder)):
        if filename.endswith(".dcm"):
            filepath = os.path.join(dicom_folder, filename)
            dicom_image = pydicom.dcmread(filepath)
            image_data = dicom_image.pixel_array
            if image_data.ndim == 2:  # Ensure the image is grayscale
                image_data = np.stack((image_data,) * 3, axis=-1)  # Convert to RGB
            images.append(Image.fromarray(image_data))
    return images

def create_montage(images, rows, cols):
    assert len(images) <= rows * cols, "More images than montage slots available"
    width, height = images[0].size
    montage_width = cols * width
    montage_height = rows * height
    montage = Image.new('RGB', (montage_width, montage_height))
    for idx, image in enumerate(images):
        x = (idx % cols) * width
        y = (idx // cols) * height
        montage.paste(image, (x, y))
    return montage

def encode_image(image, preprocess, model):
    image_tensor = preprocess(image).unsqueeze(0).to(device)
    with torch.no_grad():
        features = model.encode_image(image_tensor)
    return features

