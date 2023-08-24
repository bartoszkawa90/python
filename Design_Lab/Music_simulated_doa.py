import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt


def tdoa(doa):
    velocity=343
    microphone_array = np.array([  # Receiver position(s) [x y z] (m)
        [1.98, 2.98,  1.8],  
        [1.98, 3.02,  1.8], 
        [2.02, 2.98,  1.8], 
        [2.02, 3.02,  1.8]])
    
    direction_vector=np.array((np.cos(doa/180*np.pi),np.sin(doa/180*np.pi),0))
    t_doa=np.zeros(microphone_array.shape[1])
    t_doa=microphone_array@direction_vector/velocity
    return t_doa 


def MUSIC(R, M, thetas,freq):
    D = np.size(thetas)
    eig_val, eig_vect = np.linalg.eig(R)
    ids = np.abs(eig_val).argsort()[:(M-D)]  
    En = eig_vect[:,ids]
    
    #Ren = np.dot(En, En.conj().T)

    peak_range = np.arange(360)
    L = np.size(peak_range)
    
    Pmusic = np.zeros(L)
    
    A=np.zeros((M,L),dtype='complex').reshape(M,L)
    
    for i in range(L):
        A[:, i]=np.exp(-1j*2*np.pi*freq*tdoa(peak_range[i]).reshape(1,M))
        A[0] = 1
        #Pmusic[i] = 1/abs(np.dot(A[:, i].conj().T, np.dot(Ren, A[:, i])))
        Pmusic[i] = 1/scipy.linalg.norm((A[:,i].conj().T@En@En.conj().T@A[:,i]))
        
    Pmusic = 10 * np.log10(Pmusic / np.min(Pmusic))    
    
    return Pmusic, peak_range





doa=[100,150,250]
thetas = np.array((doa)) / 180 * np.pi  # Incoming signal directions 
w = np.array((0.55,0.76,0.20))*2*np.pi  # Emitted frequencies corresponding to incoming signals
N = 200                                 # snapshots (number of samples)
M = 4                                   # number of receivers/mics
D = np.size(thetas)                     # number of sources
var = 0.1                              # variance of noise
freq = 1000                             # center frequency of signal

#steering matrix 
A=np.zeros((M,D),dtype='complex').reshape(M,D)
for i in range(D):
    A[:,i]=np.exp(-1j*2*np.pi*freq*tdoa(doa[i]).reshape(1,M))
A[0]=1
S = 2 * np.exp(1j*(np.kron(w, np.arange(N)).reshape((D, N))))
Noise = var * np.random.randn(M, N)
X = np.dot(A, S) #Noise      #X=AS + Noise
R = X@X.conj().T     #covariance matrix

Pmusic, peak_range = MUSIC(R, M,thetas,freq)


plt.figure(figsize=(12, 7))
plt.plot(peak_range, Pmusic, '-k')
plt.xlabel('angle [degree]')
plt.ylabel('amplitude [db]')
plt.title('MUSIC for DOA')
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(peak_range*np.pi/180,Pmusic,'k')
plt.show()







