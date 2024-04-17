from scipy.optimize import minimize
initial_weights = np.ones(T) / T
constraints = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1})

result = minimize(objective, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)



### differential one has been the best
