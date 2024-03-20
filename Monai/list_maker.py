import os
import json
from pydicom import dcmread

def scan_dicom_files(directory):
    dicom_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.dicom'):
                dicom_path = os.path.join(root, file)
                
                dicom_files.append({'image': dicom_path})
     
    return dicom_files

def create_monai_json(dicom_files, json_filename):
    with open(json_filename, 'w') as f:
        json.dump(dicom_files, f, indent=4)

