

# Create a custom colormap with a large number of distinct colors
num_classes = 400
cmap = ListedColormap(plt.cm.tab20.colors[:num_classes])

# Plot the SHaP summary plot with the custom colormap
shap.summary_plot(shap_values, X_test, feature_names=vectorizer.get_feature_names(), class_names=class_names, color=cmap)
