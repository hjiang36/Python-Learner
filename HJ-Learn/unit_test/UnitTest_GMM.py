__author__ = 'Killua'

from cluster.GMM import GMM
import numpy as np
import matplotlib.pyplot as plt

# Generate data
n_samples = 100  # number of samples
n_features = 2   # number of features
data = np.random.randn(n_samples, n_features)
data[0:n_samples/2, ] += 2

# KMeans Clustering
gmm = GMM()
labels = gmm.fit_and_predict(data, hard_assign=True)

# Visualize
data_x = data[:, 0]
data_y = data[:, 1]
plt.scatter(data_x[np.nonzero(labels)[0]], data_y[np.nonzero(labels)[0]], c='r')
plt.scatter(data_x[np.nonzero(labels-1)[0]], data_y[np.nonzero(labels - 1)[0]], c='b')
plt.interactive(False)
plt.show()
