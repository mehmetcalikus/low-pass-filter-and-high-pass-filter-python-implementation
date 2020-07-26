#Mehmet Çalıkuş
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavf
import math
from math import pi


def LPF(dB, cutOffFrequency, sampleRate, X):
    #Initialize variables
    A = B = C = D = 0
    # Array to hold filtered values
    Y_out = [] 
 
    
    # There are 3 constant factors in the z-transform.                                          # wc = 2*pi*cutOffFrequency
    c1 = ((2*pi*cutOffFrequency)/((2*sampleRate)+(2*pi*cutOffFrequency)))**2                    # (wc / ((wc + 2 * fs)))^2
    c2 = ((4*sampleRate-4*pi*cutOffFrequency)/((2*sampleRate)+(2*pi*cutOffFrequency)))          # (4 * fs - 2 * wc) / (wc + 2 * fs)
    c3 = (((2*sampleRate)-(2*pi*cutOffFrequency))/((2*sampleRate)+(2*pi*cutOffFrequency)))**2   # ((2 * fs - wc ) / (wc + 2 * fs)) ^ 2
    

    # gain is calculated this way due to the definition 20*log|H(w)| = G dB
    gain = 10**(dB/20)
   
   
    for i in X:
        Y = gain*c1*i + 2*c1*A*gain + gain*c1*B + c2*C - c3*D
        Y_out.append(Y)
        B = A
        A = i
        D = C
        C = Y
    return  Y_out


#High pass filter for part C
def HPF(sampleRate, originalsignal):
    lPasszero = LPF(0, 2000, sampleRate, originalsignal)
    index = 0
    Y_out = []

    for origin in originalsignal:
        Y_out.append(origin - lPasszero[index])
        index = index + 1

    return Y_out


sampleRate, data = wavfile.read('Africa.wav')
#44100Hz = samplerate


# operations about 0dB part of PartB
zerogain = LPF(0, 2000, sampleRate, data)
arr = np.asarray(zerogain, dtype=np.int16)
out_f1 = 'Africa0dBGainLPF.wav'
wavf.write(out_f1, sampleRate, arr)


# operations about 5dB part of PartB
fivegain = LPF(5, 2000, sampleRate, data)
arr = np.asarray(fivegain, dtype=np.int16)
out_f2 = 'Africa5dBGainLPF.wav'
wavf.write(out_f2, sampleRate, arr)


#operations about Africa part of part C (High Pass Filter)
partC_Africa = HPF(sampleRate, data)
arr = np.asarray(partC_Africa, dtype=np.int16)
out_f3 = 'AfricaHPF.wav'
wavf.write(out_f3, sampleRate, arr)



sampleRate, data = wavfile.read('WinnerTakesAll.wav')


# operations about 0dB part of winnertakesall song
zerogainWinner = LPF(0, 2000, sampleRate, data)
arr = np.array(zerogainWinner, dtype=np.int16)
out_file1 = 'WinnerTakesAll0dBGainLPF.wav'
wavf.write(out_file1, sampleRate, arr)


# operations about 5dB part of winnertakesall song
fivegainWinner = LPF(5, 2000, sampleRate, data)
arr = np.array(fivegainWinner,dtype = np.int16)
out_file2 = "WinnerTakesAll5dBGainLPF.wav"
wavf.write(out_file2, sampleRate, arr)


# operations about winnertakesall song of part C (High Pass Filter)
partC_Winner = HPF(sampleRate, data)
arr = np.asarray(partC_Winner, dtype=np.int16)
out_file3 = "WinnerTakesAllHPF.wav"
wavf.write(out_file3, sampleRate, arr)
