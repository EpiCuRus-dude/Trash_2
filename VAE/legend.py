
legend_labels = [f'Label {label}: Color {color}' for label, color in label_color_map.items()]
handles = [plt.Line2D([0], [0], marker='o', color='w', label=lbl,
                      markerfacecolor=color, markersize=10) for lbl, color in zip(legend_labels, label_color_map.values())]
ax.legend(handles=handles, title='Label Colors')


ax.legend(handles=legend_handles, title='Labels', loc='upper left', bbox_to_anchor=(1, 1))


plt.tight_layout()


plt.show()
