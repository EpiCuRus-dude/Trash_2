import pydicom

def get_dicom_tags_as_text(dicom_path):
   
    dicom_file = pydicom.dcmread(dicom_path)

  
    tag_text_list = []


    for tag in dicom_file.dir():
        if tag != "PixelData":  # Exclude image data
            value = getattr(dicom_file, tag, "")
            if value:
               
                text = str(value).strip()

         
                tag_text_list.append(f"{tag}: {text}")


    all_tags_text = ' | '.join(tag_text_list)

    return all_tags_text

def pp(dicom_path, processor):
   
    dicom_file = pydicom.dcmread(dicom_path)
    image_data = dicom_file.pixel_array
    image = Image.fromarray(image_data).convert('RGB')
    text_data = get_dicom_tags_as_text(dicom_path)

    
    

    return inputs
