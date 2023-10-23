import pandas as pd
from sklearn.model_selection import train_test_split

# Load your CSV file into a Pandas DataFrame
df = pd.read_csv('your_csv_file.csv')

# Assuming 'lakes' is the column in which you want to perform stratified sampling (replace with your actual column name)
stratify_column = 'lakes'

# Perform stratified sampling
sampled_df, remaining_df = train_test_split(df, test_size=1000, stratify=df[stratify_column], random_state=42)

# 'sampled_df' now contains 1000 stratified samples, and 'remaining_df' contains the rest of the data

# You can save these dataframes to separate CSV files if needed
sampled_df.to_csv('sampled_data.csv', index=False)
remaining_df.to_csv('remaining_data.csv', index=False)
