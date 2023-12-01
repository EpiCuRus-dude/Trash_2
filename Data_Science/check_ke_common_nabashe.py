import pandas as pd

def test_and_extract_common_entries(file1, file2, columns):
    
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

   
    df1_selected = df1[columns]
    df2_selected = df2[columns]

    
    common = pd.merge(df1_selected, df2_selected, on=columns, how='inner')

    
    if common.empty:
        print("No common entries found.")
    else:
        print("Common entries found.")

    return common

