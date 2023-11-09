
color_list = ['green', 'red', 'red', 'blue', 'yellow', 'pink', 'orange', 'purple', 'brown', 'grey', 'cyan', 'magenta']


df = pd.DataFrame(values, index=models, columns=labels)


unique_values = np.unique(df.values) 
color_mapping = {val: color_list[i] for i, val in enumerate(unique_values)} 


cmap = LinearSegmentedColormap.from_list("custom_cmap", [color_mapping[val] for val in unique_values])
