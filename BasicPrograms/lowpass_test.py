# tests for my functions used for lowpass filters
import unittest
import numpy as np
from FUNCTIONS_FOR_LOWPASS_FILTERS import check_stability,freqz


# unittest

freqz_example_array = [0.4, 0.41747573-0.100896164j,
                           1.0-7.77156117e-16j, 0.4+2.939152e-17j]

class TestLowpassFunc   (unittest.TestCase):

    def test_empty(self):
        self.assertEqual(check_stability(), "You did't pass any coefficients")
        self.assertEqual(freqz(), "You did't pass any coefficients")


    def test_work(self):
        self.assertEqual(check_stability([0.5, 1], 1), False)
        self.assertEqual(check_stability([1, 4, 4], [1, 4, 4]), False)
        self.assertEqual(check_stability([1, 1, 0.25], [2, -5, 8]), True)
        # self.assertEqual(all(freqz(np.array([1, 2, 3]), np.array([4, 5, 6]), 4) == np.array(freqz_example_array)), True)
        # failed
    