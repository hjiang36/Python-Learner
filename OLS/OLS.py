__author__ = 'HJ'

import numpy as np


class OLSError(Exception):
    pass


class OLS:
    """ Do OLS fit:
          Y = Z \beta + \epsilon
        Here, Y should be a n-by-1 vector and Z should be a n-by-m matrix
        Example:
            y = np.matrix('[2.1501; 4.0501; 4.0501; 9.6501; 8.7501]')
            z = np.matrix('[9 1; 10 3; 2 6; 10 10; 7 10]')
            beta_t = np.matrix([0.3, 0.8])
            ols = OLS(y, z)
            beta_hat = ols.beta
        (HJ) June, 2014
    """

    def __init__(self, y, z):
        self._y = y
        self._z = z
        self._beta = self.fit()

    def fit(self, y=None, z=None):
        # fit OLS model and compute beta
        if y is None or z is None:  # Check number of inputs
            y = self._y
            z = self._z

        if len(y) == 0 or z.size == 0:  # check if data is available
            raise OLSError('no_data', '')
        self._y = y
        self._z = z
        r, c = z.shape
        if r < c:  # Check shape of Z
            raise OLSError('bad_data', 'Z should have more rows than columns')
        if np.linalg.matrix_rank(z) != c:  # Check if Z is full rank
            raise OLSError('bad_data', 'Z should be full rank')
        self._beta = (z.T * z).I * z.T * y
        return self._beta

    def predict(self, z):  # do prediction with fitted model
        if len(self._beta) == 0:
            raise OLSError('no_fit', 'Call fit before using predict')
        return z * self._beta

    @property
    def beta_se(self):
        # compute standard deviation of fitted beta
        if len(self._beta) == 0:
            raise OLSError('no_fit', 'Call fit before using beta_se')
        sigma = np.sqrt(self.noise_power)
        return sigma * np.sqrt(np.diag((self._z.T * self._z).I))

    @property
    def noise_power(self):
        # compute estimated noise power
        r = self.residual
        result = sum(np.multiply(r, r)).tolist()
        return 1/(len(r)-1) * result[0][0]

    @property
    def residual(self):
        # return residual of fitting
        if len(self._beta) == 0:
            raise OLSError('no_fit', 'Call fit before using predict')
        return self._y - self._z * self._beta

    @property
    def y(self):
        # Get response vector y
        return self._y

    @property
    def z(self):
        # Get input data matrix z
        return self._z

    @property
    def beta(self):
        # Get fitting parameters beta
        return self._beta