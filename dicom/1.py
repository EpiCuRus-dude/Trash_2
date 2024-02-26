import pydicom

dicom_file = pydicom.dcmread('...)


modality = dicom_file.Modality  
#SeriesDescription  # E.g., 'T1', 'T2'

for tag in dicom_file:
  ...
