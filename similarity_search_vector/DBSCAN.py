import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt



N = ...
scores = ...
teams = ...


eps = 5  
min_samples = 5 
dbscan = DBSCAN(eps=eps, min_samples=min_samples)
dbscan.fit(scores.reshape(-1, 1))
clusters = dbscan.labels_


plt.scatter(np.arange(N), scores, c=clusters, cmap='viridis', marker='o')
plt.xlabel('Candidate Index')
plt.ylabel('Score')
plt.title('DBSCAN Clustering of Candidates based on Scores')
plt.show()


unique_clusters = np.unique(clusters[clusters != -1])  # Exclude noise points
cluster_means = {cluster: np.mean(scores[clusters == cluster]) for cluster in unique_clusters}


top_clusters = sorted(cluster_means, key=cluster_means.get, reverse=True)[:2]  # Top 2 clusters for example


top_candidates = np.where(np.isin(clusters, top_clusters))[0]


team_counts = np.zeros(10)  # Assuming 10 teams
for candidate in top_candidates:
    team_counts[teams[candidate]] += 1


winning_team = np.argmax(team_counts)
print(f"The winning team is Team {winning_team} with {team_counts[winning_team]} top candidates.")
