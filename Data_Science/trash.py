import matplotlib.pyplot as plt
import numpy as np




distance_range = np.linspace(df_full['distance'].min(), df_full['distance'].max(), 100)


prediction_data = pd.concat([pd.DataFrame({'category': cat, 'distance': distance_range}) for cat in df_full['category'].unique()])



    for category in df_full['category'].unique():
        category_data = df_full[df_full['kosesher2'] == category]
        ax.scatter(category_data['mos'], category_data['cos'], label=f'cosmos')

    ax.plot(prediction_data['mos'], predictions, label=f'Fitted Curve', color='black')
    ax.set_title(title)
    ax.legend()

# Setting up the plot
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 15), sharex=True)


fit_and_predict_plot(models['Linear Regression'], X_full, y_full, prediction_data, axes[0], 'Linear Regression')


plt.tight_layout()
plt.show()
