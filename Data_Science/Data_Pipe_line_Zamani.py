import pandas as pd
import random
from datetime import datetime, timedelta

# Function to generate random date between two dates
def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60)
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)

# Define the date range
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 3, 31)

# Number of samples
num_samples = 1000

# Generate random classes (labels) and dates
random_classes = [f'Class {random.randint(1, 5)}' for _ in range(num_samples)]
random_dates = [random_date(start_date, end_date) for _ in range(num_samples)]

# Create the DataFrame
df = pd.DataFrame({
    'Class': random_classes,
    'Date': random_dates
})

# Sort the DataFrame by date for better readability
df = df.sort_values('Date').reset_index(drop=True)

df.head(10)  # Display the first 10 rows

# Update the date range for the new set of data
start_date_new = datetime(2020, 4, 1)
end_date_new = datetime(2020, 9, 30)

# Number of new samples
num_samples_new = 1500

# Generate random classes (labels) and dates for the new set of data
random_classes_new = [f'Class {random.randint(1, 7)}' for _ in range(num_samples_new)]
random_dates_new = [random_date(start_date_new, end_date_new) for _ in range(num_samples_new)]

# Create a new DataFrame for the new set of data
df_new = pd.DataFrame({
    'Class': random_classes_new,
    'Date': random_dates_new
})

# Combine the old and new DataFrames
df_combined = pd.concat([df, df_new], ignore_index=True)

# Sort the combined DataFrame by date
df_combined = df_combined.sort_values('Date').reset_index(drop=True)

df_combined.tail(10)  # Display the last 10 rows to show the new data


