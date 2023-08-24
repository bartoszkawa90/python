import numpy as np
import matplotlib.pyplot as plt
from Resources import *

signal, fs = download_example_speach_file()
# noise = np.random.randn(16000,1)

real_signal = signals_generator(filename="speech0001.wav",
                                fs=fs,
                                recievers=microphone_array,
                                source=source_position,
                                Room_dimentions=room_dimensions,
                                reflection_coefficients=None,
                                reverberation_time=3.0)

real_signal = real_signal.T

vad_frames = []

for channel in real_signal:
    vad = VAD(channel)
    vad_frames.append(vad)
vad_frames = np.array(vad_frames,dtype='object')

lent = vad_frames[0].shape[0]     # limiting the number of frames in the channels
for i in range(vad_frames.shape[0]):
    if vad_frames[i].shape[0] < lent:
        lent = vad_frames[i].shape[0]

# length correction
for i in range(vad_frames.shape[0]):
    vad_frames[i] = vad_frames[i][:lent]


# ESTIMATING FREQUENCIES
# vector of all frequencies
peak_frequencies = []#np.array([])
for channel in vad_frames:
    # peak_frequencies.append(LPC_freq_estimate(channel))
    peak_frequencies = np.concatenate((peak_frequencies, LPC_freq_estimate(channel)))

# finding one most frequent peak
count = 0
for f in np.unique(peak_frequencies):
    one_freq = (peak_frequencies.tolist()).count(f)
    if one_freq > count:
        count = one_freq
        peak = int(f)


## RFFT
rfft_vad = np.zeros((vad_frames.shape[0], vad_frames[0].shape[0], vad_frames[0].shape[1]),dtype=complex)
for channel in range(vad_frames.shape[0]):
    for frame in range(vad_frames[channel].shape[0]):
        rfft_vad[channel][frame] = np.fft.rfft(vad_frames[channel][frame],1023)


# "--------------------------------------------------------------------------"

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



def MUSIC(R, M, D, freq):

    eig_val, eig_vect = np.linalg.eig(R)
    ids = np.abs(eig_val).argsort()[:(M-D)]
    En = eig_vect[:,ids]

   # Ren = np.dot(En, En.conj().T)

    peak_range = np.arange(360)
    L = np.size(peak_range)

    Pmusic = np.zeros(L)

    A=np.zeros((M,L),dtype='complex').reshape(M,L)

    for i in range(L):
        A[:,i]=np.exp(-1j*2*np.pi*freq*tdoa(peak_range[i]).reshape(1,M))
        #Pmusic[i] = 1/abs(np.dot(A[:, i].conj().T, np.dot(Ren, A[:, i])))
        #A[0]=1
        Pmusic[i] = 1/scipy.linalg.norm((A[:,i].conj()@En@En.conj().T@A[:,i].T))

    Pmusicdb = 10 * np.log10(Pmusic / np.min(Pmusic))
    Doa,_= ss.find_peaks(Pmusic,height=6)
    return Pmusicdb, peak_range,Doa
# "------------------------------------------------------------------------------------"


# def music(R,D,M,freq):
#     _,V = scipy.linalg.eig(R)
#     Qn  = V[:,D:M]
#     doa=np.arange(360)
#     Pmusic = np.zeros(doa.size)

#     for i in range(doa.size):
#         t_doa=tdoa(doa[i])
#         sv=np.exp(-1j*2*np.pi*t_doa*freq)
#         #pspectrum[i] = 1/scipy.linalg.norm((Qn.conj().T@sv))
#         Pmusic[i] = 1/scipy.linalg.norm((sv.conj().T@Qn@Qn.conj().T@sv))
#     psindB= np.log10(10*pspectrum/pspectrum.min())



#     return psindB,doa


D=1 #number of sources
M=4 # number of microphones
freq=1000

R = matrix_R(rfft_vad, peak)

Pmusicdb,peak_range,doa=MUSIC(R, M, D,freq)



plt.figure(figsize=(10,5))
plt.plot(peak_range,Pmusicdb)
plt.show()

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(peak_range*np.pi/180,Pmusicdb)
plt.show()

