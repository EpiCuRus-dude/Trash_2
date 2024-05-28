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
