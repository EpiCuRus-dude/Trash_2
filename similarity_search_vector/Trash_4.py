
contains_string = df['column_name'].str.contains('I ...')
filtered_df = df[contains_string]




df['column_name'] = df['column_name'].str.replace('I ....*', '', regex=True)
