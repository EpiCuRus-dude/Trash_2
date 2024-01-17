def concatenate_columns(row):
    a, b, c = row['A'], row['B'], row['C']
    return a if pd.isna(b) and pd.isna(c) else a + b if pd.isna(c) else a + c if pd.isna(b) else a + b + c


df['D'] = df.apply(concatenate_columns, axis=1)
