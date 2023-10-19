
np.random.seed(42)
labels = ['a', 'b', 'c', 'd', 'e']
frequencies = [200, 100, 50, 30, 20]
data = {'A': np.random.choice(labels, 400, p=[freq/sum(frequencies) for freq in frequencies])}
df = pd.DataFrame(data)

# Calculate the frequency of each label
label_freq = df['A'].value_counts().sort_index()

# Sort the frequencies
label_freq_sorted = label_freq.sort_values()

# Normalize the frequencies
total_count = label_freq_sorted.sum()
label_freq_normalized = label_freq_sorted / total_count

# Calculate quantiles for both frequency and normalized frequency
quantile_values = label_freq_sorted.quantile(q=[q/100 for q in quantiles])
quantile_values_normalized = label_freq_normalized.quantile(q=[q/100 for q in quantiles])

# Create a table to represent the quantile data
quantile_table_df = pd.DataFrame({
    'Quantile': quantiles,
    'Frequency': quantile_values.values,
    'Normalized Frequency': quantile_values_normalized.values
})

# Visualization
sns.set(font_scale=1.2)
plt.figure(figsize=(10, 2))
ax = plt.subplot(111, frame_on=False)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
quantile_table = table(ax, quantile_table_df, loc='center', colWidths=[0.2]*len(quantile_table_df.columns))
quantile_table.auto_set_font_size(False)
quantile_table.set_fontsize(12)
quantile_table.scale(2.5, 2.5)
plt.title("Quantiles of Label Frequencies", fontsize=18, y=1.8)
pdf_path_nicer = '/mnt/data/Quantile_Table_Nicer_With_Calculation.pdf'
plt.savefig(pdf_path_nicer, bbox_inches='tight', dpi=300)

pdf_path_nicer, quantile_table_df
