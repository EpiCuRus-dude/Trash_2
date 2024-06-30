import re

def extract_pirads(text):
    
    match = re.search(r"PI[-\s]?RADS\D{0,10}(\d)", text)
    if match:
        return int(match.group(1))
    else:
        return None  
