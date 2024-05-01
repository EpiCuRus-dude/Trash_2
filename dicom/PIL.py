import pydicom
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def load_and_preprocess_dicom(path, size=(256, 256)):

    dicom = pydicom.dcmread(path)
    image = dicom.pixel_array


    image = Image.fromarray(image).convert('L')  # Convert to grayscale if not already
    image = image.resize(size, Image.ANTIALIAS)  # Resize image


    image_np = np.array(image)
    image_np = image_np / np.max(image_np)


    plt.imshow(image_np, cmap='gray')
    plt.show()

    return image_np


processed_image = load_and_preprocess_dicom('path_to_your_dicom_file.dcm')
