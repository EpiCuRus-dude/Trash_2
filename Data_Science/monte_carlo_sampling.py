## Here
## Imagine df is the dataframe


for i in range(N):

    df_sample = df.sample(n=WHATEVER, replace=False, random_state=i, weights=LABEL_COLUMN)



