def extract_and_sort_segments(text, keywords):
    keywords = sorted(keywords, key=len, reverse=True)
    keywords_regex = r'\b(' + '|'.join(re.escape(keyword) for keyword in keywords) + r')\b'
    
    matches = list(re.finditer(keywords_regex, text))
    
    segment_dict = {}
    for i in range(len(matches) - 1):
        start = matches[i]
        end = matches[i + 1]
        
        segment_key = f"{start.group(0)}_{end.group(0)}"
        potential_segment = text[start.end():end.start()].strip()
        
        if not re.search(keywords_regex, potential_segment):
            if segment_key not in segment_dict:
                segment_dict[segment_key] = potential_segment


    sorted_segment_dict = {k: segment_dict[k] for k in sorted(segment_dict)}
    return sorted_segment_dict



def extract_and_order_segments(text, keywords):
    keywords_regex = r'\b(' + '|'.join(re.escape(keyword) for keyword in keywords) + r')\b'
    matches = list(re.finditer(keywords_regex, text))
    segment_dict = {}
    for i in range(len(matches) - 1):
        start_keyword = matches[i].group(0)
        end_keyword = matches[i + 1].group(0)
        segment_key = f"{start_keyword}_{end_keyword}"
        potential_segment = text[matches[i].end():matches[i + 1].start()].strip()
        if not re.search(keywords_regex, potential_segment):
            segment_dict[segment_key] = potential_segment
    return segment_dict
