import pandas as pd
import numpy as np
import random

# Generate a sample DataFrame
data = {'Label': np.random.choice(['A', 'B', 'C'], size=100),
        'Text': [f'Text {i}' for i in range(100)],
        'Date': pd.date_range(start='2021-01-01', end='2021-04-10', periods=100)}

df = pd.DataFrame(data)

start_date = '2021-01-20'
end_date = '2021-04-01'

filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
