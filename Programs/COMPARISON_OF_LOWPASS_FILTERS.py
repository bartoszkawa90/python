#  COMPARISON OF 3 LOWPASS FILTERS IN TERMS OF STABILITY 

# NumPy package
import numpy as np
# Matplotlib for plotting figures
import matplotlib.pyplot as plt
# Signal processing package
import scipy.signal as sig
# Functions
from FUNCTIONS_FOR_LOWPASS_FILTERS import check_stability,freqz

fc = 0.3
N = 1024
freq = np.linspace(0,1,N)

#2
b_no2,b_de2 = sig.iirfilter(2,fc,btype='lowpass',ftype='butter',fs=1)
ch_no2,ch_de2 = sig.iirfilter(2,fc,rp=0.1,rs=45,btype='lowpass',ftype='cheby1',fs=1)
#6
b_no6,b_de6 = sig.iirfilter(6,fc,btype='lowpass',ftype='butter',fs=1)
ch_no6,ch_de6 = sig.iirfilter(6,fc,rp=0.1,rs=45,btype='lowpass',ftype='cheby1',fs=1)
#60
b_no60,b_de60 = sig.iirfilter(60,fc,btype='lowpass',ftype='butter',fs=1)
ch_no60,ch_de60 = sig.iirfilter(60,fc,rp=0.1,rs=45,btype='lowpass',ftype='cheby1',fs=1)

#stability
print("Checking stability :")
print("Is Butterworth 2nd order filter stabile : ",check_stability(b_de2, b_no2))
print("Is Chebyshev 2nd order filter stabile : ",check_stability(ch_de2, ch_no2))
print("Is Butterworth 6th order filter stabile : ",check_stability(b_de6, b_no6))
print("Is Chebyshev 6th order filter stabile : ",check_stability(ch_de6, ch_no6))
print("Is Butterworth 60th order filter stabile : ",check_stability(b_de60, b_no60))
print("Is Chebyshev 60th order filter stabile : ",check_stability(ch_de60, ch_no60),"\n")

# response
h_b2 = freqz(b_no2,b_de2,N)
h_ch2 = freqz(ch_no2,ch_de2,N)
h_b6 = freqz(b_no6,b_de6,N)
h_ch6 = freqz(ch_no6,ch_de6,N)
h_b60 = freqz(b_no60,b_de60,N)
h_ch60 = freqz(ch_no60,ch_de60,N)

fig,axes = plt.subplots(4,2,figsize=(10,13))
axes[0,0].plot(freq,np.abs(h_b2),label = 'Butterworth 2nd')
axes[0,0].plot(freq,np.abs(h_b6),label = 'Butterworth 6th')
axes[0,0].plot(freq,np.abs(h_b60),label = 'Butterworth 60th')
axes[0,0].legend()
axes[0,0].set_title('Butterworth',fontsize=18)

axes[0,1].plot(freq,np.abs(h_ch2),label = 'Chebyshev 2nd')
axes[0,1].plot(freq,np.abs(h_ch6),label = 'Chebyshev 6th')
axes[0,1].plot(freq,np.abs(h_ch60),label = 'Chebyshev 60th')
axes[0,1].legend()
axes[0,1].set_title('Chebyshev',fontsize=18)

no = [b_no2,b_no6,b_no60,ch_no2,ch_no6,ch_no60]
de = [b_de2,b_de6,b_de60,ch_de2,ch_de6,ch_de60]
labels = ['Butterworth 2nd','Butterworth 6th','Butterworth 60th','Chebyshev 2nd','Chebyshev 6th','Chebyshev 60th']
x = 0
for num in range(1,4):
    for i in range(0,2):
        zeros, poles, gain = sig.tf2zpk(no[num+i-1+x], de[num+i-1+x])
        t = np.linspace(0, 2*np.pi, 200)
        ax = np.max((np.max(np.abs(zeros)), np.max(np.abs(poles)), 1.5))
    
        axes[num,i].plot(np.cos(t), np.sin(t), 'c--', linewidth=2)
        axes[num,i].plot(np.real(zeros), np.imag(zeros), 'ro', linewidth=4)
        axes[num,i].plot(np.real(poles), np.imag(poles), 'bx', linewidth=4)
        axes[num,i].set_xlabel('Imagine part')
        axes[num,i].set_ylabel('Real part')
        axes[num,i].set_title(labels[num+i-1+x],fontsize=19)
        axes[num,i].legend(('Unit cicle', 'Zeros', 'Poles'))
        axes[num,i].set_xlim(-ax, ax)
        axes[num,i].set_ylim(-ax, ax)
    x += 1

    
fig.tight_layout()
plt.show()