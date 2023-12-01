import pandas as pd

def trash(file1, file2, columns):
    
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    
    common = pd.merge(df1[columns], df2[columns], how='inner').drop_duplicates()

    
    count_df1, count_df2 = 0, 0

    
    common_in_df1 = pd.DataFrame(columns=df1.columns)
    common_in_df2 = pd.DataFrame(columns=df2.columns)

    
    for _, row in common.iterrows():
        matched_df1 = df1[(df1[columns] == row.values).all(axis=1)]
        matched_df2 = df2[(df2[columns] == row.values).all(axis=1)]

        count_df1 += matched_df1.shape[0]
        count_df2 += matched_df2.shape[0]

        common_in_df1 = pd.concat([common_in_df1, matched_df1], ignore_index=True)
        common_in_df2 = pd.concat([common_in_df2, matched_df2], ignore_index=True)

    print(f"Number of common rows in File 1: {count_df1}")
    print(f"Number of common rows in File 2: {count_df2}")

    return common_in_df1, common_in_df2


