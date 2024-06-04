#
import os

def collect_nn_files(root_dir):
    nn_files_dict = {}

    for entry in os.scandir(root_dir):
        if entry.is_dir() and '_' in entry.name:
            prefix = entry.name.split('_')[0]
            sub_dir_path = entry.path
            
            nn_files = []
            for sub_entry in os.scandir(sub_dir_path):
                if sub_entry.is_file() and sub_entry.name.endswith('.nn'):
                    nn_files.append(sub_entry.path)

            if prefix not in nn_files_dict:
                nn_files_dict[prefix] = []
            nn_files_dict[prefix].extend(nn_files)

    return nn_files_dict
