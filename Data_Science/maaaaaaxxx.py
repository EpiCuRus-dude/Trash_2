import pandas as pd


data = {'Group_A_Performance': [88, 95, 70, 98],
        'Group_B_Performance': [85, 90, 95, 92],
        'Other_Column1': ['A', 'B', 'C', 'D'],
        'Other_Column2': [1, 2, 3, 4]}

df = pd.DataFrame(data)

df['Max_Performance'] = df[['Group_A_Performance', 'Group_B_Performance']].max(axis=1)


best_row_index = df['Max_Performance'].idxmax()


best_row = df.loc[best_row_index]


