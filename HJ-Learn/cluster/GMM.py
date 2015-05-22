__author__ = 'Killua'

import numpy as np
import random
from scipy.stats import multivariate_normal


class GMM:
    """
    Implementation for Gaussian Mixture Model
    """
    # properties
    n_clusters = 2  # number of clusters
    n_init = 1      # number of initialization
    mu = None       # estimated mean matrix in shape of (n_features, n_clusters)
    cov = None      # estimated covariance matrix in shape of (n_features, n_features, n_clusters)
    pi = None       # estimated prior distribution for latent variable
    max_iter = 100  # maximum iteration in EM algorithm
    tol = 1e-5      # tolerance

    def __init__(self, n_cluster=2, n_init=1, max_iter=100, tol=1e-5):
        """ Construction Method for GMM
        :param n_cluster: number of clusters
        :param n_init: number of initializations
        """
        if isinstance(n_cluster, int) and n_cluster > 0:
            self.n_clusters = n_cluster
        else:
            raise ValueError("n_cluster should be positive integer")

        if isinstance(n_init, int) and n_init > 0:
            self.n_init = n_init
        else:
            raise ValueError("n_init should be positive integer")

        if isinstance(max_iter, int) and max_iter > 0:
            self.max_iter = max_iter
        else:
            raise ValueError("max_iter should be positive integer")
        self.tol = tol

    def fit(self, data):
        """ Fit Gaussian Mixture Model using EM method
        :param data: data matrix in shape of (n_samples, n_features)
        :return: best log-likelihood value achieved
        """
        n_samples, n_features = data.shape
        data = np.matrix(data)
        cur_log_like = -float("inf")
        for _ in range(self.n_init):
            # random init
            pi = np.ones(self.n_clusters)/self.n_clusters
            mu = np.array(data[random.sample(range(n_samples), self.n_clusters), ])
            cov = np.zeros((n_features, n_features, self.n_clusters))
            for i in range(self.n_clusters):
                cov[:, :, i] = np.eye(n_features, n_features)
            p = np.matrix(np.zeros((n_samples, self.n_clusters)))
            for __ in range(self.max_iter):
                # E-step
                p_new, log_like = self.predict(data, mu, cov, pi, likelihood=True)
                if np.max(np.absolute(p_new - p)) < self.tol:  # converged
                    break
                else:
                    p = p_new

                # M-step
                pi = np.mean(p, axis=0).reshape(self.n_clusters, 1)
                cov[:] = 0
                for j in range(self.n_clusters):
                    mu[:, j] = np.array(np.transpose(data) * p[:, j]).squeeze() / sum(p[:, j])
                    for i in range(n_samples):
                        cov[:, :, j] += p[i, j] * (np.transpose(data[i, :]) - mu[:, j].reshape((self.n_clusters, 1))) * \
                            (data[i, :] - np.transpose(mu[:, j]))
                    cov[:, :, j] /= sum(p[:, j])

            if log_like > cur_log_like:
                cur_log_like = log_like
                self.mu = mu
                self.cov = cov
                self.pi = pi
            return cur_log_like

    def predict(self, data, mu=None, cov=None, pi=None, hard_assign=False, likelihood=False):
        """ Predict label for each sample
        :param data: data matrix
        :param mu: mean matrix of gaussian mixture
        :param cov: covariance matrix of gaussian mixture
        :param pi: prior for latent variable
        :param hard_assign: compute hard assignment (True) or compute probability matrix (False)
        :param likelihood: indicate whether or not to return log-likelihood
        :return: estimated probability matrix or label vector (hard assign)
        """
        if mu is None:
            mu = self.mu
        if cov is None:
            cov = self.cov
        if pi is None:
            pi = self.pi

        n_samples, n_features = data.shape

        # compute probability
        p = np.zeros((n_samples, self.n_clusters))
        for i in range(self.n_clusters):
            n = multivariate_normal(mean=mu[:, i], cov=np.squeeze(cov[:, :, i]))
            for j in range(n_samples):
                # print(n.pdf(data[j, ]) * pi[i])
                p[j, i] = n.pdf(data[j, ]) * pi[i]

        # compute likelihood
        log_like = sum(np.log(np.sum(p, axis=1)))

        # normalize
        for i in range(n_samples):
            p[i, ] = p[i, ] / sum(p[i, ])

        # hard assign
        p = np.matrix(p)
        if hard_assign:
            if likelihood:
                return np.argmax(p, axis=1), log_like
            else:
                return np.argmax(p, axis=1)
        elif likelihood:
            return p, log_like
        else:
            return p

    def fit_and_predict(self, data, hard_assign=False):
        """ Fit model and predict labels (or probability matrix)
        :param data: data matrix
        :param hard_assign: compute hard assignment (True) or compute probability matrix (False)
        :return: estimated probability matrix or label vector (hard assign)
        """
        self.fit(data)
        return self.predict(data, hard_assign=hard_assign)
