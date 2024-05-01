def dicom_to_image(dicom_path, output_path):
   
    dicom = pydicom.dcmread(dicom_path)
    
    
    image_array = dicom.pixel_array
    image_array = (np.maximum(image_array, 0) / image_array.max()) * 255.0
    image_array = np.uint8(image_array)
    
    
    image = Image.fromarray(image_array)
    
    
    image.save(output_path, "PNG")
