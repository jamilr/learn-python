# Quantitative Finance. Swaps

__author__ = 'J.R.'

import unittest


class Swaps:

    def __init__(self):
        self.rounding = 6

    # calculate a fixed rate to be used for pricing a swap on a given terms structure
    # (period = number of years, annual compounding)
    def fixed_rate(self, terms, period):
        upper = (1 - self.discount_factor(terms[5], period))
        lower = 0.0
        for i in range(len(terms)):
            lower = lower + self.discount_factor(terms[i], i + 1)
        return round(upper/lower, self.rounding)

    # calculate a discount factor for a given rate and a period
    # (period = number of years, annual compounding)
    def discount_factor(self, rate, period):
        return round(1/pow((1 + rate), period), self.rounding)


class SwapsTest(unittest.TestCase):

    def test_discount_factor(self):
        rate = 0.070
        period = 1
        df = Swaps().discount_factor(rate, period)
        expected = 0.935
        self.assertEqual(expected, df)

    def test_discount_factor_for_6_years(self):
        rate = 0.088
        period = 6
        df = Swaps().discount_factor(rate, period)
        expected = 0.602874
        self.assertEqual(expected, df)

    def test_fixed_rate(self):
        print("Calculate Fixed Rate for 6-year swap for a given term structure")
        terms = [0.070, 0.073, 0.077, 0.081, 0.084, 0.088]
        period = 6
        fixed_rate_val = Swaps().fixed_rate(terms, period)
        print(fixed_rate_val)


if __name__ == '__main__':
    unittest.main()