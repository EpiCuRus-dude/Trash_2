#
import os

import os

def collect_nn_files(root_dir, expected_postfix):
    nn_files_dict = {}

    def scan_directory(directory):
        for entry in os.scandir(directory):
            if entry.is_dir():
                if '_' in entry.name:
                    prefix, postfix = entry.name.split('_', 1)
                    if postfix == expected_postfix:
                        sub_dir_path = entry.path

                        nn_files = []
                        for sub_entry in os.scandir(sub_dir_path):
                            if sub_entry.is_file() and sub_entry.name.endswith('.nn'):
                                nn_files.append(sub_entry.path)
                            elif sub_entry.is_dir():
                                scan_directory(sub_entry.path)  # Recursively scan subdirectories

                        if prefix not in nn_files_dict:
                            nn_files_dict[prefix] = []
                        nn_files_dict[prefix].extend(nn_files)
                else:
                    scan_directory(entry.path)  # Recursively scan subdirectories without the correct postfix

    scan_directory(root_dir)
    return nn_files_dict

