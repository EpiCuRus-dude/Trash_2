
color_list = ['green', 'red', 'red', 'blue', 'yellow', 'pink', 'orange', 'purple', 'brown', 'grey', 'cyan', 'magenta']





color_mapping = ...


cmap = LinearSegmentedColormap.from_list("custom_cmap", [color_mapping[val] for val in unique_values])
