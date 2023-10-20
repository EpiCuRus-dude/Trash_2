import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Number of rows in the DataFrame
num_rows = 100

# Generate 5 classes randomly distributed
labels = ['Class_' + str(i+1) for i in range(5)]
class_column = [random.choice(labels) for _ in range(num_rows)]

# Generate random dates between January 2020 and March 2020
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 3, 31)

# Create a function to generate a random date within the given range
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

date_column = [random_date(start_date, end_date) for _ in range(num_rows)]

# Create the DataFrame
df = pd.DataFrame({
    'Label': class_column,
    'Date': date_column
})

# Sort the DataFrame by Date for better visibility
df.sort_values(by='Date', inplace=True)
df.reset_index(drop=True, inplace=True)

df.head(10)  # Show the first 10 rows of the DataFrame


# Generate more rows for March 2020 to September 2020
extended_num_rows = 200  # Number of additional rows to be added

# Add labels for Class_6 and Class_7
extended_labels = ['Class_' + str(i+1) for i in range(7)]
extended_class_column = [random.choice(extended_labels) for _ in range(extended_num_rows)]

# Generate random dates between March 2020 and September 2020
extended_start_date = datetime(2020, 3, 1)
extended_end_date = datetime(2020, 9, 30)

extended_date_column = [random_date(extended_start_date, extended_end_date) for _ in range(extended_num_rows)]

# Create the extended DataFrame
extended_df = pd.DataFrame({
    'Label': extended_class_column,
    'Date': extended_date_column
})

# Concatenate the original and extended DataFrames
final_df = pd.concat([df, extended_df], ignore_index=True)

# Sort the final DataFrame by Date
final_df.sort_values(by='Date', inplace=True)
final_df.reset_index(drop=True, inplace=True)

final_df.head(10)  # Show the first 10 rows of the final DataFrame

