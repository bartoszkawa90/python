import numpy as np
import scipy.signal as ss
import soundfile as sf
import rir_generator as rir
import matplotlib.pyplot as plt

def signals_generator(filename=None,Signal=None,velocity=343.0,fs=16000,recievers=None,source=None,Room_dimentions=None,reflection_coefficients=None,reverberation_time=None,number_of_samples=4096):
    """Returns a signal depending on the number of recievers
    https://rir-generator.readthedocs.io/_/downloads/en/latest/pdf/"""
    if filename is not None:
        signal, fs = sf.read(filename, always_2d=True)      # signal from a file and sampling frequency
    else:
        signal = Signal
        fs = fs
    if reflection_coefficients == None:
        h = rir.generate(c=velocity,fs=fs,r=recievers,s=source,L=Room_dimentions,reverberation_time=reverberation_time,nsample=number_of_samples)   # impulse response
    else:
        h = rir.generate(c=velocity,fs=fs,r=recievers,s=source,L=Room_dimentions,beta=reflection_coefficients,nsample=number_of_samples)   # impulse response
    microphone_signals = ss.convolve(h[:, None, :], signal[:, :, None])     # Convolve signal with impulse response
    return microphone_signals

#EXAMPLE

c=343.0                 # Sound velocity (m/s)
r=np.array([                     # Receiver position(s) [x y z] (m)
        [2, 1.5, 1],
        [1.5, 1, 1],
        [2.5, 1, 1]
    ])
s=[2, 3.5, 2]          # Source position [x y z] (m)
L=[5, 6, 4]             # Room dimensions [x y z] (m)
beta=[0.3, 0.2, 0.5, 0.1, 0.1, 0.1]  # reflection coefficients
#reverberation_time=0.4  # Reverberation time (s) is required if beta = None
nsample=4096            # Number of output samples

# Matrix of three signals
microphone_signals = signals_generator(filename="en.wav", velocity=c, recievers=r, source=s, Room_dimentions=L, reflection_coefficients=beta, number_of_samples=nsample)
print(microphone_signals.shape)



