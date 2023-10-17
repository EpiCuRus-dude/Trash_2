df = pd.DataFrame({
    'A': ['a', 'b', 'a', 'b', 'b', 'c', 'c','b', 'd', 'd' ,'e', 'e','b', 'd', 'd','b', 'd', 'd', 'b', 'd', 'd', 'b', 'c', 'c','b', 'd', 'd' ,'e']
})

label_counts = df['A'].value_counts()
label_counts_sorted = label_counts.sort_values()

Xth_quantile = label_counts_sorted.quantile(0.25) 
Yth_quantile = label_counts_sorted.quantile(0.95) 


group1_labels = label_counts_sorted[label_counts_sorted>=Yth_quantile].index.tolist()
group2_labels = label_counts_sorted[(label_counts_sorted>=Xth_quantile) & (label_counts_sorted<Yth_quantile)].index.tolist()


group2_labels_counts_sorted = label_counts_sorted[(label_counts_sorted>=Xth_quantile) & (label_counts_sorted<Yth_quantile)]

g2_Xth_quantile = group2_labels_counts_sorted.quantile(0.25) 
g2_Yth_quantile = group2_labels_counts_sorted.quantile(0.55) 


g2_group1_labels = group2_labels_counts_sorted[group2_labels_counts_sorted>=g2_Yth_quantile].index.tolist()
g2_group2_labels = group2_labels_counts_sorted[(group2_labels_counts_sorted>=g2_Xth_quantile) & (group2_labels_counts_sorted<g2_Yth_quantile)].index.tolist()
g2_group3_labels = group2_labels_counts_sorted[group2_labels_counts_sorted<g2_Xth_quantile].index.tolist()
