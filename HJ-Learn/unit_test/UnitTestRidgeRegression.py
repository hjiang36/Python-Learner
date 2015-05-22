__author__ = 'Killua'

import matplotlib.pyplot as plt
import numpy as np
from regression.Ridge import RidgeRegression

# Generate data
n_samples = 20
beta = 2
intercept = 0.5

data = np.random.rand(n_samples, 1)
y = beta * data + intercept + 0.1 * np.random.randn(n_samples, 1)

# Fit
ridge = RidgeRegression(y, data, alpha=0.5, intercept=True)
y_hat = ridge.predict(data)

# visualize
plt.scatter(data, y)
plt.plot(data, y_hat)

plt.interactive(False)
plt.show()
