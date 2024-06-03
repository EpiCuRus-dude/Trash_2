def extract_and_concat(filename):

    matches = re.search(r"CCC_\['([^]]+?)'\]_\(([^)]+?)\)_W\.json", filename)
    if matches:

        letters = matches.group(1).replace("'", "").split(',')
        numbers = matches.group(2).split(',')
        

        return ''.join(letters + numbers)
    return None
