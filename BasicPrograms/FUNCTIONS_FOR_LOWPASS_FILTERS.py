#      FUNCTIONS FOR LOWPASS FILTERS

# NumPy package
import numpy as np
# Matplotlib for plotting figures
import matplotlib.pyplot as plt
# Signal processing package
import scipy.signal as sig

def check_stability(de=0, no=0):        # Function to check stability of the filter
    if np.sum(de)==0 or np.sum(no)==0:
        answer = "You did not pass any coefficients"
        return answer
    else:
        x = np.abs(np.roots(de))
        for i in range(x.size):
            if x[i] > 1:
                return False
        return True


def freqz(no=0, de=0, worN=512):        #  fUNCTION TO CALCULATE FREQUENCY RESPONSE OF THE FILTER
    if np.sum(no)==0 or np.sum(de)==0:
        answer = "You did not pass any coefficients"
        return answer
    else:
        h = np.zeros(worN)
        freq = np.linspace(0, 0.5, worN)
        sum1 = 0    #np.zeros(worN,dtype=complex)  
        sum2 = 0    #np.zeros(worN,dtype=complex)

        for i in range(no.size):
            sum1 += no[i] * np.exp(-2j * np.pi * i * freq)
        for j in range(de.size):
            sum2 += de[j] * np.exp(-2j * np.pi * j * freq)
        h = sum1/(sum2)
        return h

