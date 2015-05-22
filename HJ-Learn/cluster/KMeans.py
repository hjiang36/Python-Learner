__author__ = 'Killua'

import numpy as np
from math import isfinite
import random
import operator

class KMeans:
    """
    Implementation for K-means clustering
    This is the practice work for HJ and should not be used in any project
    Formal implementation of K-means can be found in sklearn.cluster.KMeans
    """

    # variables
    n_cluster = 2            # number of clusters, in sklearn, it's default to 8 instead of 2
    max_iter = 1000          # number of iteration for each initialization
    n_init = 10              # number of time the k-means to be run with different centroids
    distance_func = None     # function to compute distance between two inputs
    distance = None          # distance matrix
    centroids = None         # centroids for fitted clusters

    # construction method
    def __init__(self, n_cluster=2, max_iter=1000, n_init=10,
                 distance_func=lambda x, y: np.linalg.norm(x-y)):
        # set number of clusters
        if isinstance(n_cluster, int) and n_cluster > 0:
            self.n_cluster = n_cluster
        else:
            raise ValueError("number of clusters should be positive integer")

        # set number of iterations
        if (isinstance(max_iter, int) and max_iter > 0) or isfinite(max_iter):
            self.max_iter = max_iter
        else:
            raise ValueError("max iteration should be positive integer")

        # set number of init
        if isinstance(n_init, int) and n_init > 0:
            self.n_init = n_init
        else:
            raise ValueError("n_init should be positive integers")

        # set distance function
        if callable(distance_func):
            self.distance_func = distance_func
        else:
            raise ValueError("distance function should be callable")

    def fit(self, data, init_method="kmeans++"):
        """ Compute k-means clustering
        :param data: data matrix, shape=(n_samples, n_features)
        :param init_method: initialization method, can be "random" or "kmeans++"
        :return: centroids of clusters in shape of (n_clusters, n_features)
        """

        # Check input
        if not isinstance(data, np.ndarray):
            raise ValueError("X should be a matrix")

        n_samples, n_features = data.shape
        if self.n_cluster > n_samples:
            raise ValueError("X has too few samples to be clustered")

        # Compute distance matrix
        self.compute_dist(data)

        # do K-means with multiple initialization
        cur_wss = wss = float("inf")  # within sum of squared
        for _ in range(self.n_init):
            c_index = self.centroids_init(data, init_method)
            centroids = data[c_index, ]
            labels = np.zeros(n_samples)
            for __ in range(self.max_iter):
                new_labels, cur_wss = self.predict(data, centroids, compute_wss=True)
                # check convergence
                if (new_labels == labels).all():
                    break

                # compute new centroids
                labels = new_labels
                for i in range(self.n_cluster):
                    centroids[i, ] = np.mean(data[labels == i, ], axis=0)
            if cur_wss < wss:
                wss = cur_wss
                self.centroids = centroids
        return self.centroids

    def compute_dist(self, data):
        """ Compute distance matrix
        :param data: data matrix, shape=(n_samples, n_features)
        """
        n_samples, n_features = data.shape
        self.distance = np.zeros(shape=(n_samples, n_samples))
        for i in range(n_samples):
            for j in range(i, n_samples):
                self.distance[i, j] = self.distance[j, i] = self.distance_func(data[i, ], data[j, ])

    def predict(self, new_data, centroids=None, compute_wss=False):
        """ Predict label for new data
        :param new_data: new data matrix, shape=(n_samples, n_features)
        :return: class labels for new samples
        """
        if centroids is None:
            centroids = self.centroids
        n_samples, _ = new_data.shape
        labels = np.zeros(n_samples)
        dist2centroid = np.zeros(self.n_cluster)
        wss = 0
        for i in range(n_samples):
            for j in range(self.n_cluster):
                dist2centroid[j] = self.distance_func(new_data[i, ], centroids[j, ])
            labels[i], dist = min(enumerate(dist2centroid), key=operator.itemgetter(1))
            wss += dist
        if compute_wss:
            return labels, wss
        else:
            return labels

    def fit_and_predict(self, data, init_method="kmeans++"):
        self.fit(data, init_method)
        return self.predict(data)

    def centroids_init(self, data=[], method="random"):
        """ Initialize centroids for K-means
        :param method: method to be used to generate centroids, can be "random" or "kmeans++"
        :param data: data matrix, used for method kmeans++
        :return: centroids index in rows of data matrix
        """
        n_samples, _ = self.distance.shape
        if method == "random":
            return random.sample(range(n_samples), self.n_cluster)
        elif method == "kmeans++":
            c_index = [0 for _ in range(self.n_cluster)]
            # choose first centroid
            c_index[0] = random.sample(range(n_samples), k=1)[0]
            # compute distance
            d = [0 for _ in range(n_samples)]
            for i in range(n_samples):
                d[i] = self.distance_func(data[i, ], data[c_index[0], ])
            for i in range(1, self.n_cluster):
                # choose centroid
                c_index[i] = np.nonzero(np.random.multinomial(1, d/sum(d), size=1))[1][0]

                # update distance
                for j in range(n_samples):
                    d[j] = min(d[j], self.distance_func(data[j, ], data[c_index[i], ]))
            return c_index
        else:
            raise ValueError("Unknown input for method, only random and kmeans++ supported")