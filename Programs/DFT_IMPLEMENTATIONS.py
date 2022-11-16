#  DFT IMPLEMENTATIONS
# NumPy package
import numpy as np

# DFT
def dft(x):
  
    X = np.zeros(x.size, dtype=complex)
    N = len(x)
    for k in range(0,N):
        for n in range(0,N):
            X[k] +=  x[n] * np.exp(-2j*np.pi*k*n/N)

    return X


# MDFT
def mdft(x):

    n = np.arange(len(x))
    k = n.reshape((len(x), 1))
    e = np.exp(-2j * np.pi * k * n / len(x))
    
    X = x@e
    return X


#  FFT
def fft_radix2(x):
   
    # Check if it is a vector
    assert x.ndim == 1, 'Input array should be 1-dimensional array, i.e x.shape == (N, )'
    
    # Number of samples in X
    N = x.size
    
    # Check if input array has proper shape
    assert np.log2(N).is_integer(), 'Number of samples should be 2**k'
  
    k = np.arange(N)
    if N==1:
        X=x
    else:
        Xp = fft_radix2(x[::2])   #  z % bedzie zwracać wartości parzyste albo nie a nie indeksy
        Xn = fft_radix2(x[1::2])
        wk = np.exp(-2j * np.pi * k  / N)
        
        X = np.concatenate([Xp + wk[:int(N/2)]*Xn,Xp + wk[int(N/2):]*Xn]) # wk /2 bo Xp i Xn to juz sa połówki X
    
    return X