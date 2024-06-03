def extract_and_concat(filename):

    matches = re.search(r"CCC_\['([^]]+?)'\]_\(([^)]+?)\)_W\.json", filename)
    if matches:

        letters = matches.group(1).replace("'", "").split(',')
        numbers = matches.group(2).split(',')
        

        return ''.join(letters + numbers)
    return None

plt.figure(figsize=(10, 6))
plt.bar(df_sorted['FileName'], df_sorted['Value'], color='blue')
plt.xlabel('File Name')
plt.ylabel('Value')
plt.title('Bar Plot of Values Sorted Low to High')
plt.xticks(rotation=90)  # Set rotation to 90 degrees for vertical labels
plt.show()
