import os
import shutil
import pandas as pd
import pydicom

dir1 = "path/to/dir1"
dir2 = "path/to/dir2"
dir5 = "path/to/dir5"
dir7 = "path/to/dir7"
dir8 = "path/to/dir8"

access_num_to_id_date = {}
csv_files_dir1 = [f for f in os.listdir(dir1) if f.endswith('.csv')]

for csv_file in csv_files_dir1:
    df = pd.read_csv(os.path.join(dir1, csv_file))
    for idx, row in df.iterrows():
        if row['access_num'] in access_num_to_id_date:
            continue
        access_num_to_id_date[row['access_num']] = (row['id'], row['date'])

if not os.path.exists(dir8):
    os.makedirs(dir8)

csv_files_dir7 = [f for f in os.listdir(dir7) if f.endswith('.csv')]
for csv_file in csv_files_dir7:
    df_dir7 = pd.read_csv(os.path.join(dir7, csv_file))
    for idx, row in df_dir7.iterrows():
        for access_num, (id_val, date_val) in access_num_to_id_date.items():
            if row['id'] == id_val and row['date'] == date_val:
                sub_dir_path = os.path.join(dir8, access_num)
                if not os.path.exists(sub_dir_path):
                    os.makedirs(sub_dir_path)
                dicom_src_path = os.path.join(dir5, access_num)
                if os.path.exists(dicom_src_path):
                    for dicom_file in os.listdir(dicom_src_path):
                        shutil.copy(os.path.join(dicom_src_path, dicom_file), sub_dir_path)
                sub_csv_path = os.path.join(sub_dir_path, csv_file)
                if not os.path.exists(sub_csv_path):
                    df_dir7.iloc[[idx]].to_csv(sub_csv_path, index=False)
                else:
                    df_dir7.iloc[[idx]].to_csv(sub_csv_path, mode='a', header=False, index=False)
                break

print("Files have been organized in dir8 based on matches found.")
