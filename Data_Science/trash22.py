
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
