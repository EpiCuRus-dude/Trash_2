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

    keywords_regex = r'(' + '|'.join(re.escape(keyword) for keyword in keywords) + r')(?!\w)'
    matches = list(re.finditer(keywords_regex, text))
    segment_dict = {}
    used_segments = set()
    for i in range(len(matches) - 1):
        start = matches[i]
        end = matches[i + 1]
        potential_segment = text[start.end():end.start()].strip()
        if not re.search(keywords_regex, potential_segment):
            segment_key = f"{start.group(0)}_{end.group(0)}"
            if potential_segment not in used_segments:
                segment_dict[segment_key] = potential_segment
                used_segments.add(potential_segment)
    return segment_dict




def extract_and_order_segments(text, keywords):
    keywords_regex = r'(' + '|'.join(re.escape(keyword) for keyword in keywords) + r')(?!\w)'
    matches = list(re.finditer(keywords_regex, text))
    segment_dict = {}
    used_segments = set()
    for i in range(len(matches) - 1):
        start = matches[i]
        end = matches[i + 1]
        potential_segment = text[start.end():end.start()].strip()
        if not re.search(keywords_regex, potential_segment):
            segment_key = f"{start.group(0)}_{end.group(0)}"
            if potential_segment not in used_segments:
                segment_dict[segment_key] = potential_segment
                used_segments.add(potential_segment)
    
    
    if matches:
        last_match = matches[-1]
        last_segment = text[last_match.end():].strip()
        if not re.search(keywords_regex, last_segment):
            last_key = f"{last_match.group(0)}_end"
            if last_segment not in used_segments:
                segment_dict[last_key] = last_segment
                used_segments.add(last_segment)
                
    return segment_dict





