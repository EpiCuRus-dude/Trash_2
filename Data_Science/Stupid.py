def extract_between_keywords_with_repeats(text, keywords):

    keywords = [re.escape(keyword) for keyword in keywords]


    results = {}

 
    keyword_positions = {keyword: [m.start() for m in re.finditer(keyword, text, re.IGNORECASE)] for keyword in keywords}

  
    for keyword1, keyword2 in combinations(keyword_positions.keys(), 2) + [(k, k) for k in keyword_positions]:
        positions1 = keyword_positions[keyword1]
        positions2 = keyword_positions[keyword2]
        for start in positions1:
            for end in positions2:
                if start < end:
                    # Extract text between these positions
                    pattern = f"({re.escape(text[start:end])})"
                    match = re.search(pattern, text[start:end], re.IGNORECASE | re.DOTALL)
                    if match:
                        key = f"{keyword1}_to_{keyword2}"
                        segment = match.group(1).strip()
                        if key in results:
                            results[key].append(segment)
                        else:
                            results[key] = [segment]

    return results
