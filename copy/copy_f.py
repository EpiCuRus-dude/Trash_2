import os
import shutil


all_results_dir = 'all_results'
os.makedirs(all_results_dir, exist_ok=True)


for item in os.listdir('.'):
    if os.path.isdir(item) and item.startswith("Search"):
        search_folder_path = os.path.join('.', item)
        dest_folder_path = os.path.join(all_results_dir, item)
        os.makedirs(dest_folder_path, exist_ok=True)

     
        for subfolder in os.listdir(search_folder_path):
            if subfolder.startswith("Summary"):
                summary_folder_path = os.path.join(search_folder_path, subfolder)

               
                for file in os.listdir(summary_folder_path):
                    if file.endswith(".json") and file.startswith("res"):
                        src_file_path = os.path.join(summary_folder_path, file)
                        dest_file_path = os.path.join(dest_folder_path, file)
                        shutil.copy2(src_file_path, dest_file_path)

print("All files have been successfully copied.")
