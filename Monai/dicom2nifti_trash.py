import dicom2nifti
import os

def dicom_to_nifti(dicom_dir, output_dir):
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    
    dicom2nifti.convert_directory(dicom_dir, output_dir)


