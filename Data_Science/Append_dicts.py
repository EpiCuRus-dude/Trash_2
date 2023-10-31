from collections import defaultdict

# Initialize the master dictionary
master_dict = defaultdict(list)

def update_master_dict(new_dict):
    for key, value in new_dict.items():
        
        value = value if isinstance(value, list) else [value]
        master_dict[key].extend(value)
