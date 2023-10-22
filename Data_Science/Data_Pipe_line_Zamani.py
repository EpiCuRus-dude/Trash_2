import pandas as pd
import numpy as np
from datetime import datetime, timedelta


start_date1 = datetime.strptime("2020-01-01", "%Y-%m-%d")
end_date1 = datetime.strptime("2020-03-31", "%Y-%m-%d")
delta1 = end_date1 - start_date1

data1 = {
    "date": [start_date1 + timedelta(days=np.random.randint(0, delta1.days)) for _ in range(200)],
    "class": np.random.randint(1, 6, 200)  # Classes from 1 to 5
}

df1 = pd.DataFrame(data1)
df1 = df1.sort_values(by="date")

# Generate random data for March 2020 to Sep 2020 (Classes 1 to 7)
start_date2 = datetime.strptime("2020-03-01", "%Y-%m-%d")
end_date2 = datetime.strptime("2020-09-30", "%Y-%m-%d")
delta2 = end_date2 - start_date2

data2 = {
    "date": [start_date2 + timedelta(days=np.random.randint(0, delta2.days)) for _ in range(300)],
    "class": np.random.randint(1, 8, 300)  # Classes from 1 to 7
}

df2 = pd.DataFrame(data2)
df2 = df2.sort_values(by="date")

## need to be continued

# Combine both dataframes
df = pd.concat([df1, df2], ignore_index=True)

# Show the first few rows of the dataframe
df.head()


from torch.utils.data import Dataset, DataLoader
import torch



# Convert the Date column to datetime format and sort the DataFrame by Date
df_combined['Date'] = pd.to_datetime(df_combined['Date'])
df_combined.sort_values('Date', inplace=True)

# Create time-based groups (e.g., group by every 3 days)
time_window = '3D'  # 3 days
groups = df_combined.groupby(pd.Grouper(key='Date', freq=time_window))

# Create a list of (start, end) indices for each time group
group_indices = []
start_idx = 0
for name, group in groups:
    end_idx = start_idx + len(group)
    if len(group) > 0:
        group_indices.append((start_idx, end_idx))
    start_idx = end_idx


