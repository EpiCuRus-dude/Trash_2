import os
import shutil
import pandas as pd
import pydicom

dir1 = "path/to/dir1"
dir2 = "path/to/dir2"
dir4 = "path/to/dir4"
dir5 = "path/to/dir5"

csv_files = [f for f in os.listdir(dir1) if f.endswith('.csv')]

accession_to_dicom = {}

def find_dicom_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".dcm"):
                dicom_path = os.path.join(root, file)
                try:
                    dicom_data = pydicom.dcmread(dicom_path, force=True)
                    accession_number = dicom_data.get("AccessionNumber", None)
                    if accession_number:
                        if accession_number not in accession_to_dicom:
                            accession_to_dicom[accession_number] = []
                        accession_to_dicom[accession_number].append(dicom_path)
                except Exception as e:
                    print(f"Error reading DICOM file {dicom_path}: {e}")

find_dicom_files(dir2)

if not os.path.exists(dir4):
    os.makedirs(dir4)
if not os.path.exists(dir5):
    os.makedirs(dir5)

matched_series_count = {}

for csv_file in csv_files:
    csv_path = os.path.join(dir1, csv_file)
    df = pd.read_csv(csv_path)
    dicom_paths = []
    for _, row in df.iterrows():
        access_num = row.get("access_num")
        if access_num in accession_to_dicom:
            dicom_paths.append(accession_to_dicom[access_num])
            sub_dir_path = os.path.join(dir5, access_num)
            if not os.path.exists(sub_dir_path):
                os.makedirs(sub_dir_path)
            for dicom_file in accession_to_dicom[access_num]:
                shutil.copy(dicom_file, sub_dir_path)
            sub_csv_path = os.path.join(sub_dir_path, csv_file)
            df[df['access_num'] == access_num].to_csv(sub_csv_path, index=False)
            matched_series_count[access_num] = len(set(accession_to_dicom[access_num]))
        else:
            dicom_paths.append([])
    df["dicom_files"] = dicom_paths
    new_csv_path = os.path.join(dir4, csv_file)
    df.to_csv(new_csv_path, index=False)

print(f"Matched DICOM series counts: {matched_series_count}")
