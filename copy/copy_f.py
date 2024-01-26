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

tarball_name = 'all_results.tar.gz'
with tarfile.open(tarball_name, "w:gz") as tar:
    tar.add(all_results_dir, arcname=os.path.basename(all_results_dir))




zip_filename = 'all_results.zip'
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(all_results_dir):
        for file in files:
            zipf.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(all_results_dir, '..')))

