import pandas as pd

def test_and_extract_common_entries(file1, file2, columns):
   
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    
    df1_selected = df1[columns]
    df2_selected = df2[columns]

   
    common = pd.merge(df1_selected, df2_selected, on=columns, how='inner')

    
    common_in_df1 = pd.merge(df1, common, on=columns, how='inner')
    common_in_df2 = pd.merge(df2, common, on=columns, how='inner')

   e
    count_df1 = common_in_df1.shape[0]
    count_df2 = common_in_df2.shape[0]

    print(f"Number of common rows in File 1: {count_df1}")
    print(f"Number of common rows in File 2: {count_df2}")

    return common_in_df1, common_in_df2


columns_to_check = ['A', 'B', 'C']
common_in_file1, common_in_file2 = test_and_extract_common_entries('file1.csv', 'file2.csv', columns_to_check)
print("Common in File 1:")
print(common_in_file1)
print("\nCommon in File 2:")
print(common_in_file2)
