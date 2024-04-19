from scipy.optimize import minimize
initial_weights = np.ones(T) / T
constraints = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1})
result = differential_evolution(objective, bounds, constraints=cons)

result = minimize(objective, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)



### differential one has been the best

 weights = np.array(weights)
  scores = np.array(scores)

  weighted_scores = scores * weights
  total_scores_per_candidate = np.sum(weighted_scores, axis=1)

  mean_score = np.mean(total_scores_per_candidate)
  variance = np.var(total_scores_per_candidate)


  regularization_term = lambda_reg * np.sum(weights**2)


  regularized_variance = variance + regularization_term

cons = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1})
def median_score(scores):
    return [sorted(candidate)[len(candidate) // 2] for candidate in scores]


median_scores = median_score(scores)
