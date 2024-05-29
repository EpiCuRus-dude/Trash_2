import pandas as pd


data = {
    'Column1': [1, 2, 3, 4],
    'Column2': ['abc', 'xyz123', 'def', 'ghi'],
    'Column3': ['xyz567', 'mno', 'pqr', 'stu']
}
df = pd.DataFrame(data)


prefix_to_check = 'xyz'


mask = df.apply(lambda col: col.astype(str).str.startswith(prefix_to_check))


rows_with_prefix = df[mask.any(axis=1)]

print(f"Rows with values having the prefix '{prefix_to_check}':")
print(rows_with_prefix)
