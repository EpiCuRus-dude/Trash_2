from sklearn.ensemble import IsolationForest

def select_top_candidates_outliers(scores, contamination=0.1):
    scores = np.array(scores).reshape(-1, 1)
    iso_forest = IsolationForest(contamination=contamination)
    outliers = iso_forest.fit_predict(scores)
    top_candidates_indices = np.where(outliers == 1)[0]
    return top_candidates_indices


scores = np.random.randint(0, 101, 100)
top_candidates_indices = select_top_candidates_outliers(scores, contamination=0.1)
