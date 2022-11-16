# tests for my functions used for lowpass filters
import unittest
from FUNCTIONS_FOR_LOWPASS_FILTERS import check_stability,freqz


#def test_empty():
    #assert check_stability() == "You_did't_pass_any_coefficients"
    #assert freqz() is "You did't pass any coefficients"

#def test_with_some_coefficients():
    #assert check_stability([0.5,1],1) is False
    #assert check_stability([1,4,4],[1,4,4]) is False
   # assert check_stability([1,1,0.25],[2,-5,8]) is True


# unittest

class TestCezarCode(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(check_stability(),"You did't pass any coefficients")
        self.assertEqual(freqz(),"You did't pass any coefficients")

    def test_work(self):
        self.assertEqual(check_stability([0.5,1],1),False)
        self.assertEqual(check_stability([1,4,4],[1,4,4]),False)
        self.assertEqual(check_stability([1,1,0.25],[2,-5,8]),True)

    