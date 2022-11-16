#   COMPARISON OF DFT IMPLEMENTATION

# Time utils
import time
# NumPy package
import numpy as np
# Matplotlib for plotting figures
from matplotlib import pyplot as plt
# DFT
from  DFT_IMPLEMENTATIONS import dft,mdft,fft_radix2

# Number of repetitions for each test point on characteristic
R = 10

# Dictionary containing DFT implementation with corresponding K value
DFT_IMPLEMENTATIONS_LIST = {
    'dft':        (dft, 7),
    'mdft':       (mdft, 11),
    'fft_radix2': (fft_radix2, 12),
    'fft':        (np.fft.fft, 15),
}

# This is a dict where i store (test_N, time)
# where test_N is a vector containing number of samples of tested function
# and time is a vector that containing mean execution time for signal of length N from test_N
results = {
    'dft':        None,
    'mdft':       None,
    'fft_radix2': None,
    'fft':        None,
}


K = DFT_IMPLEMENTATIONS_LIST['dft'][1]
N=np.asarray([2**k for k in range(1,K+1)])
ti = np.zeros(len(N))
test_N = np.zeros(len(N))

for k in range(len(N)):
    #print(k)
    timee = np.zeros(R,)
    t_d = np.arange(0,0.1,0.1/(N[k]))
    test_N[k] = len(t_d)
    x_d = np.cos(t_d)
    for j in range(R):
        
        t_start = time.time()
        time.sleep(0.0005)
        x_d = dft(x_d)
        t_end = time.time()

        timee[j] = t_end - t_start
        
    ti[k] = np.mean(timee)
results['dft'] = (test_N,ti)


K = DFT_IMPLEMENTATIONS_LIST['mdft'][1]
N=np.asarray([2**k for k in range(1,K+1)])
ti = np.zeros(len(N))
test_N = np.zeros(len(N))

for k in range(len(N)):
    #print(k)
    timee = np.zeros(R,)
    t_d = np.arange(0,0.1,0.1/(N[k]))
    test_N[k] = len(t_d)
    x_d = np.cos(t_d)
    for j in range(R):
        
        t_start = time.time()
        time.sleep(0.0005)
        x_d = mdft(x_d)
        t_end = time.time()

        timee[j] = t_end - t_start
        
    ti[k] = np.mean(timee)
results['mdft'] = (test_N,ti)


K = DFT_IMPLEMENTATIONS_LIST['fft_radix2'][1]
N=np.asarray([2**k for k in range(1,K+1)])
ti = np.zeros(len(N))
test_N = np.zeros(len(N))

for k in range(len(N)):
    #print(k)
    timee = np.zeros(R,)
    t_d = np.arange(0,0.1,0.1/(N[k]))
    test_N[k] = len(t_d)
    x_d = np.cos(t_d)
    for j in range(R):
        
        t_start = time.time()
        time.sleep(0.0005)
        x_d = fft_radix2(x_d)
        t_end = time.time()

        timee[j] = t_end - t_start
        
    ti[k] = np.mean(timee)
results['fft_radix2'] = (test_N,ti)


K = DFT_IMPLEMENTATIONS_LIST['fft'][1]
N=np.asarray([2**k for k in range(1,K+1)])
ti = np.zeros(len(N))
test_N = np.zeros(len(N))

for k in range(len(N)):
    #print(k)
    timee = np.zeros(R,)
    t_d = np.arange(0,0.1,0.1/(N[k]))
    test_N[k] = len(t_d)
    x_d = np.cos(t_d)
    for j in range(R):
        
        t_start = time.time()
        time.sleep(0.0005)
        x_d = np.fft.fft(x_d)
        t_end = time.time()

        timee[j] = t_end - t_start
        
    ti[k] = np.mean(timee)
results['fft'] = (test_N,ti)


fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 5), dpi=100)

for name, (test_N, r) in results.items():
    ax.plot(test_N, r, 'o-', label=name)

ax.set_xscale('log', base=2)
ax.set_yscale('log', base=10)
    
ax.set_ylabel('Mean time to compute DFT [s]')
ax.set_xlabel('Numer of samples')
ax.legend()
ax.grid()
plt.show()
