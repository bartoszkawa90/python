# tests for my functions used for lowpass filters

# NumPy package
import numpy as np
# Matplotlib for plotting figures
import matplotlib.pyplot as plt
# Signal processing package
import scipy.signal as sig

import pytest
from FUNCTIONS_FOR_LOWPASS_FILTERS import check_stability, freqz


def test_empty():
    assert check_stability() == "You did not pass any coefficients"
    assert freqz() == "You did not pass any coefficients"

def test_with_some_coefficients():
    assert check_stability([0.5, 1], 1) is False
    assert check_stability([1, 4, 4], [1, 4, 4]) is False
    assert check_stability([1, 1, 0.25], [2, -5, 8]) is True