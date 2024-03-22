import pydicom

def infer_mri_weighting(dicom_file_path):
    dicom_data = pydicom.dcmread(dicom_file_path)
    
   
    protocol_name = getattr(dicom_data, 'ProtocolName', '').lower()
    if 't1' in protocol_name:
        return 'T1-weighted'
    elif 't2' in protocol_name:
        return 'T2-weighted'
    elif 'dw' in protocol_name or 'diffusion' in protocol_name:
        return 'Diffusion-weighted'
    
    
    tr = float(dicom_data.RepetitionTime)
    te = float(dicom_data.EchoTime)
    
   
    if tr < 1000 and te < 30:
        return 'T1-weighted'
    elif tr > 2000 and te > 60:
        return 'T2-weighted'
    
    
    if hasattr(dicom_data, 'DiffusionBValue') and float(dicom_data.DiffusionBValue) > 0:
        return 'Diffusion-weighted'
    
    return 'Unknown'
