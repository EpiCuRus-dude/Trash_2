import pandas as pd


data = {
    'A': [1, 2, 3, 4, 5, 6],
    'B': [7, 8, 9, 10, 11, 12],
    'C': ['label1', 'label2', 'label1', 'label3', 'label2', 'label3']
}
df = pd.DataFrame(data)


max_samples = df['C'].value_counts().max()


balanced_df = pd.DataFrame()
for label in df['C'].unique():
    label_df = df[df['C'] == label]
    replicated_df = pd.concat([label_df] * (max_samples // len(label_df)), ignore_index=True)
    
    remaining_rows = max_samples % len(label_df)
    if remaining_rows > 0:
        replicated_df = pd.concat([replicated_df, label_df.iloc[:remaining_rows]], ignore_index=True)
    balanced_df = pd.concat([balanced_df, replicated_df], ignore_index=True)


print(balanced_df)
