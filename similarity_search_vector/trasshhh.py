import pandas as pd
from sklearn.cluster import KMeans

data = pd.DataFrame({
    'score': [92, 85, 70, 88, 75, 95, 60, 78, 55, 82, 90, 67, 76, 80, 85],
    'team': ['A', 'B', 'A', 'B', 'C', 'A', 'C', 'A', 'B', 'C', 'B', 'A', 'C', 'A', 'B']
})

k = 3
kmeans = KMeans(n_clusters=k)
data['cluster'] = kmeans.fit_predict(data[['score']])

cluster_avg_score = data.groupby('cluster')['score'].mean().sort_values(ascending=False)
top_clusters = cluster_avg_score.index[:1]

top_candidates = data[data['cluster'].isin(top_clusters)]
team_counts = top_candidates['team'].value_counts()

winning_team = team_counts.idxmax()
print(f"The winning team is: {winning_team}")
