__author__ = 'Killua'

from cluster.KMeans import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Generate data
n_samples = 100  # number of samples
n_features = 2   # number of features
data = np.random.randn(n_samples, n_features)
data[0:n_samples/2, ] += 2

# KMeans Clustering
kmeans = KMeans()
labels = kmeans.fit_and_predict(data)

# Visualize
plt.scatter(data[labels == 0, 0], data[labels == 0, 1], c='r')
plt.scatter(data[labels == 1, 0], data[labels == 1, 1], c='b')
plt.interactive(False)
plt.show()