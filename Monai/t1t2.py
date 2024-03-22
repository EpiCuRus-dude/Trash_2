import pydicom

def infer_mri_weighting_advanced(dicom_file_path):
    dicom_data = pydicom.dcmread(dicom_file_path)
    
    def check_protocol_and_sequence_names(data):
        for attr in ['ProtocolName', 'SequenceName']:
            val = getattr(data, attr, '').lower()
            if any(x in val for x in ['t1']):
                return 'T1-weighted'
            if any(x in val for x in ['t2']):
                return 'T2-weighted'
            if any(x in val for x in ['dw', 'diff', 'diffusion']):
                return 'Diffusion-weighted'
            if any(x in val for x in ['flair', 'stir']):
                return 'T2-weighted (FLAIR/STIR)'
        return ''

    name_based_weighting = check_protocol_and_sequence_names(dicom_data)
    if name_based_weighting:
        return name_based_weighting
    
    tr = dicom_data.get('RepetitionTime', 0)
    te = dicom_data.get('EchoTime', 0)
    ti = dicom_data.get('InversionTime', -1)

    if tr and te:
        if tr < 800 and te < 30:
            return 'T1-weighted'
        elif ti > 0 and te > 80:
            return 'T2-weighted (FLAIR/STIR)'
        elif tr > 2000 and te > 80:
            return 'T2-weighted'
    
    if hasattr(dicom_data, 'DiffusionBValue'):
        b_value = dicom_data.DiffusionBValue
        if b_value and float(b_value) > 0:
            return 'Diffusion-weighted'
    
    if hasattr(dicom_data, 'SpectralSelection') or 'fat sat' in dicom_data.ProtocolName.lower():
        return 'Potential Fat Suppression Technique Used'

    return 'Unknown - Requires Manual Review'


