# Not related to here!
legend_labels = [f'Label {label}: Color {color}' for label, color in label_color_map.items()]
handles = [plt.Line2D([0], [0], marker='o', color='w', label=lbl,
                      markerfacecolor=color, markersize=10) for lbl, color in zip(legend_labels, label_color_map.values())]
ax.legend(handles=handles, title='Label Colors')


ax.legend(handles=legend_handles, title='Labels', loc='upper left', bbox_to_anchor=(1, 1))


plt.tight_layout()


plt.show()


for label in encoded_data:
    encoded_data[label] = np.array(encoded_data[label])

# Dictionary for outliers
outliers = {label: [] for label in range(14)}

# Define a threshold for Z-score, e.g., 3
threshold = 3


for label, data in encoded_data.items():
    if len(data) == 0:
        continue

    
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)

    
    z_scores = np.abs((data - mean) / std)

    
    outlier_indices = np.where(np.any(z_scores > threshold, axis=1))[0]

    
    outliers[label] = data[outlier_indices]
