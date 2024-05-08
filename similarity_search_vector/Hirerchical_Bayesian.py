import pymc3 as pm
import numpy as np
import theano.tensor as tt


np.random.seed(42)
scores = np.array([75, 82, 90, 68, 95, 84, 70, 89, 78, 91, 77, 96, 81, 85, 88, 93, 69, 87, 83, 86])
teams = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3])  # Teams


with pm.Model() as model:
    
    mu = pm.Normal('mu', mu=85, sd=10)
    sigma = pm.HalfNormal('sigma', sd=10)
    
    
    team_effects = pm.Normal('team_effects', mu=0, sd=1, shape=len(np.unique(teams)))
    
    
    individual_effects = pm.Normal('individual_effects', mu=0, sd=1, shape=len(scores))
    
    
    expected_scores = mu + team_effects[teams] + individual_effects
    
    
    likelihood = pm.Normal('likelihood', mu=expected_scores, sd=sigma, observed=scores)

  
    trace = pm.sample(500, return_inferencedata=False)
