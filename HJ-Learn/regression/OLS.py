__author__ = 'Killua'

import numpy as np


class OLS:
    """ Ordinary Least Square
    """

    # variable
    beta = None        # regression coefficient
    y = None           # regression output
    data = None        # regression input
    intercept = False  # whether to add intercept term

    # methods
    def __init__(self, y=None, data=None, intercept=False):
        """ Construction method for OLS class
        :param y: regression output
        :param data: regression input in shape of (n_samples, n_features)
        """
        y = np.matrix(y)
        data = np.matrix(data)

        self.y = y
        self.data = data
        self.intercept = intercept
        if y is not None and data is not None:
            self.fit(y, data)

    def fit(self, y, data):
        """ fitting least square coefficient
        :param y: regression output
        :param data: regression input data
        :return: regression coefficient
        """
        # Check input
        if y.shape[0] != data.shape[0]:
            raise ValueError("Size mismatch between regression input and output")
        # Process
        y = np.matrix(y)
        self.y = y
        if self.intercept:
            data = np.lib.pad(data, ((0, 0), (1, 0)), "constant", constant_values=1)
        data = np.matrix(data)
        self.data = data

        # Fit
        self.beta = np.linalg.inv(np.transpose(data) * data) * np.transpose(data) * y
        return self.beta

    def predict(self, new_data):
        """ predict for new data
        :param new_data: new data input
        :return: predicted regression output
        """
        if self.intercept:
            new_data = np.lib.pad(new_data, ((0, 0), (1, 0)), "constant", constant_values=1)
        new_data = np.matrix(new_data)
        return new_data * self.beta
