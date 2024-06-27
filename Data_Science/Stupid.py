
import re

def extract_segments(text, keywords):
    keywords = sorted(keywords, key=len, reverse=True)
    keywords_regex = r'\b(' + '|'.join(re.escape(keyword) for keyword in keywords) + r')\b'
    
    matches = list(re.finditer(keywords_regex, text))
    
    segments = set()
    for i in range(len(matches) - 1):
        start = matches[i]
        end = matches[i + 1]
        potential_segment = text[start.end():end.start()].strip()
        
        if not re.search(keywords_regex, potential_segment):
            segments.add(potential_segment)

    return list(segments)

