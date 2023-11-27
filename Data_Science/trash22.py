
for column in df.columns:
    if df[column].dtype == object:  
        unique_values = df[column].unique()
        if 'YES' in unique_values or 'NO' in unique_values:
            print(f"Column '{column}' contains 'YES'/'NO' values.")


rows_with_yes = []


for index, row in df.iterrows():
    if 'YES' in row.values:
        rows_with_yes.append(index)


print("Rows containing 'YES':", rows_with_yes)


import csv
from datasets import load_dataset, Features, Value


with open('dddd.csv', 'r') as file:
    reader = csv.reader(file)
    columns = next(reader)


features = Features({col: Value('string') for col in columns})


dataset = load_dataset('csv', data_files='your_file.csv', features=features)


