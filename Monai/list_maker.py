import os
import json
from pydicom import dcmread


def scan_dicom_files(directory):
    dicom_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.dicom'):
                dicom_path = os.path.join(root, file)
                dicom_files.append(dicom_path)
    return dicom_files

def split_data(files, validation_ratio=0.2):
    random.shuffle(files)
    split_idx = int(len(files) * validation_ratio)
    validation_files = files[:split_idx]
    training_files = files[split_idx:]
    return training_files, validation_files

def create_monai_json(training_files, validation_files, json_filename):
    dataset = {
        'training': [{'image': path} for path in training_files],
        'validation': [{'image': path} for path in validation_files]
    }
    with open(json_filename, 'w') as f:
        json.dump(dataset, f, indent=4)

