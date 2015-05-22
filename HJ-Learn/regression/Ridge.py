__author__ = 'Killua'

import numpy as np


class RidgeRegression:
    """
    Implementation of ridge regression
    """
    # properties
    beta = None   # estimated coefficient
    y = None      # regression output
    data = None   # regression input
    alpha = 0   # penalty term
    intercept = False  # whether to include intercept

    def __init__(self, y=None, data=None, alpha=0, intercept=False):
        """ Construction method
        :param data: regression input
        :param y: regression output
        :param alpha: penalty term
        :param intercept: whether to include intercept
        :return:
        """
        self.data = data
        self.y = y
        self.alpha = alpha
        self.intercept = intercept

        if data is not None and y is not None:
            self.fit(y, data)

    def fit(self, y, data):
        """ Fit ridge regression model
        :param data: regression input
        :param y: regression output
        :return: fitted beta
        """
        if self.intercept:
            data = np.pad(data, ((0, 0), (1, 0)), "constant", constant_values=1)

        # Process
        y = np.matrix(y)
        self.y = y
        data = np.matrix(data)
        self.data = data

        # Fit
        _, n_features = data.shape
        self.beta = np.linalg.inv(np.transpose(data) * data + self.alpha * np.eye(n_features)) * np.transpose(data) * y
        return self.beta

    def predict(self, new_data):
        """ Predict for new data
        :param new_data: new data input
        :return: estimated regression output
        """
        if self.intercept:
            new_data = np.lib.pad(new_data, ((0, 0), (1, 0)), "constant", constant_values=1)
        new_data = np.matrix(new_data)
        return new_data * self.beta

    def fit_and_predict(self, data, y):
        self.fit(data, y)
        return self.predict(data)
