
def compare_dicom_files(file1_path, file2_path):

    dicom1 = pydicom.dcmread(file1_path)
    dicom2 = pydicom.dcmread(file2_path)


    dicom1_dict = {tag: dicom1[tag].value for tag in dicom1.dir()}
    dicom2_dict = {tag: dicom2[tag].value for tag in dicom2.dir()}


    differences = []

    all_keys = set(dicom1_dict.keys()).union(dicom2_dict.keys())

    for key in all_keys:
        value1 = dicom1_dict.get(key, None)
        value2 = dicom2_dict.get(key, None)
        if value1 != value2:
            differences.append((key, value1, value2))
