import numpy as np
import scipy.signal as ss
import soundfile as sf
import rir_generator as rir
from pathlib import Path
import requests
import scipy.linalg


def signals_generator(filename=None,Signal=None,velocity=343.0,fs=16000,recievers=None,source=None,Room_dimentions=None,reflection_coefficients=None,reverberation_time=None,number_of_samples=4096,order=0):
    """Returns a signal depending on the number of recievers
    https://rir-generator.readthedocs.io/_/downloads/en/latest/pdf/"""
    if filename is not None:
        signal, fs = sf.read(filename, always_2d=True)      # signal from a file and sampling frequency
    else:
        signal = Signal
        fs = fs
    if reflection_coefficients == None:
        h = rir.generate(c=velocity,fs=fs,r=recievers,s=source,L=Room_dimentions,reverberation_time=reverberation_time,nsample=number_of_samples,order=order)   # impulse responseS
    else:
        h = rir.generate(c=velocity,fs=fs,r=recievers,s=source,L=Room_dimentions,beta=reflection_coefficients,nsample=number_of_samples,order=order)   # impulse response
    microphone_signals = ss.convolve(h, signal)     # Convolve signal with impulse response

    return microphone_signals


def download_example_speach_file(add_noise = False):
    """Downloads a sample speech file for the current localization, filename is  'speech0001.wav'
       Returns data ( signal samples ) and  fs ( sampling frequency )"""
    url = "http://sp-class.agh.edu.pl/samples/speech0001.wav"

    if not isinstance('speech0001.wav', Path):
        path = Path('speech0001.wav')
    if not path.is_file():
        r = requests.get(url)
        with open(path, "wb") as f:
            f.write(r.content)

    data, fs = sf.read('speech0001.wav', always_2d=True)
    data = data / np.abs(data.max())
    if add_noise:
        noise = np.random.randn(13000)
        data = np.concatenate((noise/abs(max(noise)),data,noise/abs(max(noise))), axis=None)

    return data, fs


def VAD(sig, rate=512, overlap=256):
    """example : speech_frames=VAD(data,rate=512,overlap=256)
       rate is window size=512, overlap=256, sig=data from wavfile"""
    
    #overlap signal
    overlapped_frames =[]
    for i in range(0, len(sig), int((overlap))):
        
        split= np.array((sig[i:i + rate]))
        # window_frame = ss.convolve(split,np.hanning(rate)) #apply window
        overlapped_frames.append(split)
        
    N_frames=len(overlapped_frames)
    #end overlap
    
    #calculate frame energy and zero_crossings
    energy=np.zeros(N_frames)
    Zcr=np.zeros(N_frames)
    time=np.zeros(N_frames)
    
    for i in range (N_frames):
        
        energy[i]=np.abs(1/len(overlapped_frames[i])*np.sum(((overlapped_frames[i])**2)))
        Zcr[i]=0.5*np.sum(abs(np.sign(overlapped_frames[i][1:])-np.sign(overlapped_frames[i][0:len(overlapped_frames[i])-1])))                   
   #end energy / Zcr

    #Thresholds
    E_thres=np.mean(energy)/2
    Zcr_thres=(3/2)*np.mean(Zcr)-0.3*np.std(Zcr)
    #end Thresholds
    
    #vad decision
    vad_frames=[]
    
    for i in range(N_frames):
        if (energy[i] > E_thres and Zcr[i] < Zcr_thres):
            vad_frames.append(overlapped_frames[i])
    #end vad decision


    # # Plot detected speech -optional
    # vad=np.zeros(N_frames)
    # time=np.zeros(N_frames)
    # for i in range(N_frames):
    #     time[i]=rate/2 + (i+1)*overlap
    #     if (energy[i] >=E_thres and Zcr[i] < Zcr_thres):
    #         vad[i]=max(sig)
    # time_sec=np.arange(0,len(sig)/fs,1/fs)
    # vad=np.interp(np.arange(len(sig)),time,vad)
    #
    # fig,axes=plt.subplots(1,1,figsize=(14,7))
    # axes.plot(time_sec,sig)
    # axes.plot(time_sec,vad,"r")
    # # end plot

    return np.array(vad_frames)  #return a vector which every element is speech frame


# Functions to calculate LPC spectrum
 
def autocorr(vad_frames, lag=10):
        c = np.correlate(vad_frames,vad_frames, 'full')
        mid = len(c)//2
        acov = c[mid:mid+lag]
        acor = acov/acov[0]
        return(acor)
    
def LPC_coeff(vad_frames, order):
        ac = autocorr(vad_frames,order+1)
        R = scipy.linalg.toeplitz(ac[:order])
        r = ac[1:order+1]
        phi = scipy.linalg.inv(R).dot(r)
        a = np.concatenate([np.ones(1), -phi])
        return a

def LPC_freq_estimate(vad_frames, order=80, height=15):
    """vad_frames : vector of frames after VAD
    Returns indexes of peak frequencies for every frame in vad_frames"""
    N_frames=len(vad_frames)
    freqs=np.linspace(0,8000,512)
    peak_freqs = []
    for i in range(N_frames):
        a=LPC_coeff(vad_frames[i],order)
        w, h = ss.freqz(1,a)
        h_db=10*np.log10(np.abs(h))
        freq_index, _ = ss.find_peaks(h_db,height)  # we want frequency indexes for which fft values are at least above 15 dB
        peak_freqs.append(freq_index)
    
    return np.concatenate(peak_freqs).ravel()


def matrix_R(rfft_vad, peak):
    """ rfft_vad : fft from vad frames for each channel
        peak : index of peak frequency from LPC spectrum
    Returns correlation R matrix """
    xi = np.zeros((rfft_vad.shape[0],1),dtype=complex)
    R = np.zeros((rfft_vad.shape[0], rfft_vad.shape[0]), dtype=complex)
    for frame in range(rfft_vad[0].shape[0]):
        for channel in range(rfft_vad.shape[0]):
            xi[channel] = rfft_vad[channel][frame][peak]
        R += np.outer(xi, xi.conj())

    return R * (1/rfft_vad[0].shape[0])   #  N =>  Number of frames   rfft_vad[0].shape[0]


def srp_phat(x, micarray, freqs=[], fs = 16000):
    '''Function calculating srp-phat

    Parameters
    ----------
    x : matix [m,l]
        m - number of microphones (signals from micrphones)
    micarray : matirx [m,col]
        where col are cooridinates [x,y,z] (matrix with microphones possitions)
    fs : int
        sampling frequency (default: 16000 Hz)
    
    
    Returns
    --------
    array
        srp-phat (powers)
    array
        teta - angles used in scanning
    '''
    
    grid=360
    m=x.shape[0]
    teta=np.linspace(0,2*np.pi,grid)
    look_vec=np.array((np.cos(teta),np.sin(teta),np.zeros(grid)))

    L=x.shape[1]
    pp=ss.firwin(31,(500,4000),pass_zero = False, fs=fs)
    x=ss.lfilter(pp,1,x)
    x*=np.hanning(L)
    X=np.fft.rfft(x,2*L)
    fre=fs/L
    Y=np.zeros((m,L+1),complex)
    P=np.zeros(grid,complex)
    
    for i in range(grid):
        for l in range(m):
            steer_delay=micarray[l]@look_vec.T[i]/343
            if(len(freqs)>0):
                for k in freqs:
                    Y[l,k] = X[l,k]/np.abs(X[l,k])*np.exp(-1j*(np.pi*k*fre*steer_delay))
            else:
                for k in range(160,L):
                    Y[l,k] = X[l,k]/np.abs(X[l,k])*np.exp(-1j*(np.pi*k*fre*steer_delay))
        YY=np.sum(Y,0)
        P[i]=YY@np.conjugate(YY)
    return P,teta


def VAD1(frame):
    """VAD dla jednej ramki, zwraca TRUE albo FALSE"""
  
    #calculate frame energy and zero_crossings
    energy=np.abs(1/len(frame)*np.sum(((frame)**2)))
    Zcr=0.5*np.sum(abs(np.sign(frame[1:])-np.sign(frame[0:len(frame)-1])))                   
   #end energy / Zcr
    #Thresholds
    E_thres=1.8e-05
    Zcr_thres=70
    if (energy > E_thres and Zcr < Zcr_thres):
        return True
    else:
        return False
    

def split_to_frames(x,L,overlap):
    '''Dzieli sygnał na ramki'''
    frames = []
    frames2 = []
    frames3 = []
    frames4 = []

    for i in range(0, x.shape[1]-500, int((overlap))):

        split= np.array((x[0,i:i + L]))
        split2= np.array((x[1,i:i + L]))
        split3= np.array((x[2,i:i + L]))
        split4= np.array((x[3,i:i + L]))        # window_frame = ss.convolve(split,np.hanning(rate)) #apply window

        frames.append(split)
        frames2.append(split2)
        frames3.append(split3)
        frames4.append(split4)

    return np.stack((frames,frames2,frames3,frames4),1)

# Variables
velocity = 343.0                 # Sound velocity (m/s)
microphone_array = np.array([                     # Receiver position(s) [x y z] (m)
        [1.0, 1.0, 1.0],
        [0.1, 1.0, 1.0],
        [1.0, 0.1, 1.0]])
source_position = [5.0, 5.0, 1.8]       # Source position [x y z] (m)
room_dimensions = [6.0, 6.0, 3.0]       # Room dimensions [x y z] (m)
beta=[0.3, 0.2, 0.5, 0.1, 0.1, 0.1]  # example of reflection coefficients



#EXAMPLE OF USING RIR_generator

# download_example_speach_file()
# #reverberation_time=0.4  # Reverberation time (s) is required if beta = None
# nsample=4096            # Number of output samples
# # Matrix of three signals
# microphone_signals = signals_generator(filename="speech0001.wav", velocity=velocity, recievers=microphone_array, source=source_position, Room_dimentions=room_dimensions, reflection_coefficients=beta, number_of_samples=nsample)
# print(microphone_signals.shape)



