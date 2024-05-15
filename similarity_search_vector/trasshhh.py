import numpy as np
from sklearn.metrics import silhouette_score

# Sample data: replace with your actual scores
np.random.seed(42)
N = 100
scores = np.random.uniform(0, 100, N)


ranked_indices = np.argsort(scores)[::-1]  # Indices of scores in descending order


silhouette_scores = []
for k in range(2, N):
    top_k_indices = ranked_indices[:k]
    labels = np.zeros(N)
    labels[top_k_indices] = 1
    silhouette_scores.append(silhouette_score(scores.reshape(-1, 1), labels))


optimal_k = np.argmax(silhouette_scores) + 2 
print(f"The optimal number of top candidates (k) is: {optimal_k}")

####################

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


np.random.seed(42)
N = 100
scores = np.random.uniform(0, 100, N)


ranked_indices = np.argsort(scores)[::-1]  # Indices of scores in descending order


sse = []
for k in range(1, N + 1):
    top_k_scores = scores[ranked_indices[:k]]
    mean_top_k = np.mean(top_k_scores)
    sse.append(np.sum((top_k_scores - mean_top_k) ** 2))


second_derivative = np.diff(np.diff(sse))
elbow_point = np.argmin(second_derivative) + 2  # Adding 2 to adjust for the double diff

print(f"The optimal number of top candidates (k) using the elbow method is: {elbow_point}")

# Plot the elbow graph for visualization
plt.plot(range(1, N + 1), sse, marker='o')
plt.axvline(x=elbow_point, color='r', linestyle='--')
plt.xlabel('Number of Top Candidates (k)')
plt.ylabel('Sum of Squared Differences')
plt.title('Elbow Method for Optimal k')
plt.show()


#######################
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample data: replace with your actual scores
np.random.seed(42)
N = 100
scores = np.random.uniform(0, 100, N)

def gap_statistic(data, nrefs=20, max_k=10):
    shape = data.shape
    tops = data.max(axis=0)
    bottoms = data.min(axis=0)
    dists = np.matrix(np.diag(tops - bottoms))

    refs = np.random.random_sample(size=(shape[0], nrefs)) * dists + bottoms

    gaps = np.zeros((max_k,))
    for k in range(1, max_k + 1):
        km = KMeans(n_clusters=k)
        km.fit(data)
        disp = km.inertia_

        refdisps = np.zeros(refs.shape[1])
        for j in range(refs.shape[1]):
            km.fit(refs[:, j].reshape(-1, 1))
            refdisps[j] = km.inertia_
        
        gap = np.log(np.mean(refdisps)) - np.log(disp)
        gaps[k-1] = gap

    return gaps

# Reshape scores for the function
scores_reshaped = scores.reshape(-1, 1)
gaps = gap_statistic(scores_reshaped, max_k=10)

# Find the optimal k using the gap statistic
optimal_k = np.argmax(gaps) + 1  # Adding 1 because k starts from 1
print(f"The optimal number of top candidates (k) using the gap statistic is: {optimal_k}")

# Plot the gap statistic
plt.plot(range(1, 11), gaps, marker='o')
plt.xlabel('Number of Top Candidates (k)')
plt.ylabel('Gap Statistic')
plt.title('Gap Statistic for Optimal k')
plt.show()


