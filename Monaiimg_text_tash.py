import pydicom
from PIL import Image

def extract_image_and_text(dicom_path):
  
    dicom = pydicom.dcmread(dicom_path)

   
    image = dicom.pixel_array
    image = Image.fromarray(image).convert('RGB')  # Convert to RGB image

   
    text_data = f"{dicom.StudyDescription} {dicom.SeriesDescription}"  

    return image, text_data
