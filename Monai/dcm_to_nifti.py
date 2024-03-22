import os
import subprocess
import json

def convert_dicom_to_nifti(dicom_dir, nifti_output_dir):
   
    
    os.makedirs(nifti_output_dir, exist_ok=True)
    
    
    command = ['dcm2niix', '-o', nifti_output_dir, dicom_dir]
    subprocess.run(command, capture_output=True)
    
  
    for file in os.listdir(nifti_output_dir):
        if file.endswith(".nii") or file.endswith(".nii.gz"):
            return os.path.join(nifti_output_dir, file)

def find_dicom_series_and_convert(base_dir, nifti_base_dir):
    mapping = {}
    
    for root, dirs, files in os.walk(base_dir):
        
        dicom_files = [f for f in files if f.endswith('.dcm')]
        if dicom_files:
            
            relative_path = os.path.relpath(root, base_dir)
            nifti_output_dir = os.path.join(nifti_base_dir, relative_path)
            
            
            nifti_path = convert_dicom_to_nifti(root, nifti_output_dir)
            if nifti_path:
                mapping[root] = nifti_path
                
    
    with open("dicom_to_nifti_mapping.json", "w") as json_file:
        json.dump(mapping, json_file, indent=4)


base_dir = "dir1" 
nifti_base_dir = "nifti_files" 
find_dicom_series_and_convert(base_dir, nifti_base_dir)
