def extract_between_keywords(text, keywords):
    
    keywords = [re.escape(keyword) for keyword in keywords]


    results = {}

  
    for i in range(len(keywords) - 1):
        pattern = f"{keywords[i]}(.*?){keywords[i + 1]}"
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:

            key = f"{keywords[i]}_to_{keywords[i + 1]}"
            results[key] = match.group(1).strip()

    return results
