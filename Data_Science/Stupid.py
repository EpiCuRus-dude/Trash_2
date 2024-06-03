def extract_and_concat(filename):

    matches = re.search(r"CCC_\['([^]]+?)'\]_\[?([^)\]]+?)\]?_W\.json", filename)
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


# Generate a color map
colors = plt.cm.viridis(np.linspace(0, 1, len(df_sorted)))

# Plotting
plt.figure(figsize=(15, 8))  # Increase figure size for better visibility
bars = plt.bar(df_sorted['FileName'], df_sorted['Value'], color=colors, width=0.4)  # Apply color map to bars
plt.xlabel('File Name')
plt.ylabel('Value')
plt.title('Bar Plot of Values Sorted Low to High')
plt.xticks(rotation=90, fontsize=10)  # Set rotation to 90 degrees for vertical labels and smaller font size
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add a grid for better readability
plt.ylim(0, 50)  # Specify the range for the y-axis
plt.tight_layout()  # Adjust layout to fit everything nicely
plt.show()
