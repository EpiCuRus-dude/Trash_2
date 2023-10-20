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
