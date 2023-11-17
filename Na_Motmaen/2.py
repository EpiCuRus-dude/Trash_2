import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import dirichlet, norm


alpha = [2, 3, 5]


dirichlet_samples = dirichlet(alpha).rvs(1000)


mu, sigma = 0, 1  


gaussian_samples = norm.rvs(mu, sigma, 1000)


plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist2d(dirichlet_samples[:, 0], dirichlet_samples[:, 1], bins=50, cmap='Blues')
plt.xlabel('Probability of Class 1')
plt.ylabel('Probability of Class 2')
plt.title('Dirichlet Distribution')


plt.subplot(1, 2, 2)
plt.hist(gaussian_samples, bins=50, density=True, alpha=0.6, color='r')
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, sigma)
plt.plot(x, p, 'k', linewidth=2)
plt.title('Gaussian Distribution')
plt.xlabel('Value')
plt.ylabel('Density')

plt.tight_layout()
plt.show()
