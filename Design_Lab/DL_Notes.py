import numpy as np
import scipy.signal as ss
import soundfile as sf
import rir_generator as rir
from pathlib import Path
import requests
import scipy.linalg

lista = [0]
lis = [1,2,3,45,6]
print(lista+lis)
a = np.array([[1, 2], [3, 4]])
print(a)
print(np.concatenate(a))