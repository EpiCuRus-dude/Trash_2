import re


file_paths = [
    '/something/something_else/res_10.json',
    '/something/something_else/res_100.json',
    '/something/something_else/res_50.json',
    '/something/something_else/res_500.json'
]

def extract_number(file_path):
    
    file_name = file_path.split('/')[-1]
    
    match = re.search(r'\d+', file_name)
    if match:
        return int(match.group())
    return 0  # Return 0 if no number is found


sorted_file_paths = sorted(file_paths, key=extract_number)

print(sorted_file_paths)
