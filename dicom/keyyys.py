import itertools

def generate_combinations(keys, numbers):
    all_combinations = []

    # Generate combinations with different lengths
    for r_keys in range(1, len(keys) + 1):
        for r_numbers in range(1, len(numbers) + 1):
            key_combos = list(itertools.combinations(keys, r_keys))
            number_combos = list(itertools.combinations(numbers, r_numbers))
            for key_combo in key_combos:
                for number_combo in number_combos:
                    all_combinations.append([key_combo, number_combo])
    
    return all_combinations



keys = ['key1', 'key2', 'key3']
numbers = [1, 2, 3, 4, 5, 6]

combinations = generate_combinations(keys, numbers)

# Print the combinations
for combo in combinations:
    print(combo)


keyword_counts = Counter(all_keywords)


labels, values = zip(*keyword_counts.items())


sorted_indices = np.argsort(values)
labels = np.array(labels)[sorted_indices]
values = np.array(values)[sorted_indices]


plt.figure(figsize=(10, 8))
plt.barh(labels, values, color='skyblue')
plt.xlabel('Frequency')
plt.ylabel('Keywords')
plt.title('Keyword Frequencies')
plt.show()

all_pi_numbers = [float(num) for sublist in df['pi_numbers'] for num in sublist]

plt.figure(figsize=(10, 6))
plt.hist(all_pi_numbers, bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Pi Numbers')
plt.ylabel('Frequency')
plt.title('Distribution of Pi Numbers')
plt.show()


def extract_pirads_context(description):
    context_list = []
    
    sentences = re.split(r'[.!?]', description)
    
    for sentence in sentences:
        # Use regex to match variations like "PI-RAD v1", "PI-RAD 1", "PI-RADS v2", etc.
        matches = re.finditer(r'(\b\w+\b\s+)?(\bPI-RADS?\s*v?\d*\s*\d*\b)(\s+\b\w+\b)?', sentence, re.IGNORECASE)
        for match in matches:
            context = match.groups()
            context_list.append(context)

    if not context_list:
        return None
    
    return context_list
