import unittest

import numpy as np
from src.maths.splines import natural_cubic_spline

class SplinesTest(unittest.TestCase):
    def test_natural_cubic_spline_with_no_prior(self):
        xs = np.array([1, 4, 6, 7, 15])
        ys = np.random.rand(len(xs))

        solution = natural_cubic_spline(xs, ys, 0, ys)
        np.testing.assert_array_almost_equal(ys, solution, decimal=3)

    def test_natural_cubic_spline_with_large_prior(self):
        xs = np.array([1, 4, 6, 7, 15])
        ys = np.random.rand(len(xs))
        ys_prior = xs ** 2

        solution = natural_cubic_spline(xs, ys, 1e8, ys_prior)
        np.testing.assert_array_almost_equal(ys_prior, solution, decimal=3)