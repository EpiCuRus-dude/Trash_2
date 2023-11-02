
unique_values = df['Column A'].unique()
train_val_values, test_values = train_test_split(unique_values, test_size=0.2, random_state=42)  # Adjust the test_size as necessary

train_val_df = df[df['Column A'].isin(train_val_values)]
test_df = df[df['Column A'].isin(test_values)]
