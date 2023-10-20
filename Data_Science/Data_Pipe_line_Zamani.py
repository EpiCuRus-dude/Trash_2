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
