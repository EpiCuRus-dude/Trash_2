import pymc3 as pm
import numpy as np

data = 
N, C = data.shape

with pm.Model() as model:
    qualities = pm.Normal('qualities', mu=0, sigma=1, shape=C)
    reliabilities = pm.HalfNormal('reliabilities', sigma=1, shape=N)
    
    for i in range(N):
        pm.Normal('scores_by_referee_{}'.format(i), 
                  mu=qualities, 
                  sigma=1/reliabilities[i], 
                  observed=data[i])

    trace = pm.sample(1000, return_inferencedata=False)

estimated_qualities = np.mean(trace['qualities'], axis=0)
estimated_reliabilities = np.mean(trace['reliabilities'], axis=0)
weights = estimated_reliabilities / np.sum(estimated_reliabilities)

print("Estimated Qualities:", estimated_qualities)
print("Weights for Referees:", weights)
#none of them worked
