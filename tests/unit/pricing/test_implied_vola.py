import unittest

from src.pricing.implied_vola import _bs_price, bs_implied_vola


class ImpliedVola(unittest.TestCase):
    def test_bs_implied_vola(self):
        K = 100.0
        T = 0.01
        F = 100.0
        option_type = "Call"
        expected_vola = 0.25
        price = _bs_price(K, T, F, option_type, expected_vola)
        implied_vola = bs_implied_vola(K, T, F, option_type, price)
        self.assertAlmostEqual(implied_vola, expected_vola, places=10)