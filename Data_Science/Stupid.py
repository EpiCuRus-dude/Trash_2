from itertools import permutations
def extract_between_any_keywords(text, keywords):

    keywords = [re.escape(keyword) for keyword in keywords]


    results = {}

    
    for keyword1, keyword2 in permutations(keywords, 2):
        pattern = f"{keyword1}(.*?){keyword2}"
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            
            ordered_key = f"{keyword1}_to_{keyword2}"
            results[ordered_key] = match.group(1).strip()

    return results
