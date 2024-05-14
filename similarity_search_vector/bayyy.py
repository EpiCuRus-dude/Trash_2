from bayes_opt import BayesianOptimization

def evaluate_threshold(threshold, scores):
    selected_candidates = scores[scores >= threshold]
  
    return len(selected_candidates)

def bayesian_optimization_threshold(scores):
    pbounds = {'threshold': (np.min(scores), np.max(scores))}
    optimizer = BayesianOptimization(f=evaluate_threshold, pbounds=pbounds, random_state=1)
    optimizer.maximize(init_points=2, n_iter=10)
    best_threshold = optimizer.max['params']['threshold']
    return scores[scores >= best_threshold]


top_bayesian_candidates = bayesian_optimization_threshold(scores)
