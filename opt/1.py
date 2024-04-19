from scipy.optimize import minimize
initial_weights = np.ones(T) / T
constraints = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1})
result = differential_evolution(objective, bounds, constraints=cons)

result = minimize(objective, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)

##############################

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


####
def borda_count(scores):
    num_candidates = len(scores)
    return [sum((num_candidates - rank) for rank in sorted(candidate)) for candidate in zip(*scores)]


borda_scores = borda_count(scores)

#########

def borda_count(scores):
    num_candidates = len(scores)
    num_referees = len(scores[0])
    
    borda_scores = [0] * num_candidates
    
 
    for referee_scores in zip(*scores):  # This gives us each referee's scores as tuples
        # Sort scores and get original indices (ranks)
        sorted_indices = sorted(range(num_candidates), key=lambda x: referee_scores[x], reverse=True)
        # Assign points based on rank
        for rank, index in enumerate(sorted_indices):
            borda_scores[index] += num_candidates - 1 - rank
    
    return borda_scores


borda_scores = borda_count(scores)
print("Borda scores:", borda_scores)


