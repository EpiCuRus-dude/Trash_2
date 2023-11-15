import pandas as pd

# Sample DataFrame
df = pd.DataFrame({'A': [{'1': 'mm', '2': 33, '3': 'Something'}, 
                         {'1': 'xx', '2': 44, '3': 'AnotherThing'}]})

# Function to extract value for key '3'
def extract_value_from_dict(row):
    # Check if key '3' exists in the dictionary
    return row.get('3', None)  # Returns None if key '3' is not found

# Apply the function to each row in column 'A' and create a new column 'B'
df['B'] = df['A'].apply(extract_value_from_dict)

# Display the DataFrame
print(df)
