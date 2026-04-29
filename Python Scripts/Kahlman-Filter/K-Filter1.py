#zach nelson
#playing around trying to implement a Kahlman filter



from sys import exit 
import numpy as np
import math
import matplotlib.pylab as plt
import scipy.signal as signal

def RMS(s):
    return np.sqrt(np.mean(np.square(s)))

T = 10  #length of the recording in seconds
SamplingRate = 300 #in Hz 
N = T*SamplingRate #total number of samples

index = np.arange(N)    #counts 1,2,3 ..
timestep = index/SamplingRate #counts up to 10 by 1/300

#signal Parameters
W1 = 10
W2 = 50
pi = math.pi

#Noise Parameters
mu, sigma = 0,2

########################################
##########Generate a Signal#############
########################################

###generate a sequence consisting of multuple sine functions

#numpy sin takes in angle in radians
DC = np.ones(N) * 0.25
sin1 = np.sin(timestep*W1)
sin2 = np.sin(timestep*W2 + pi/2)

#compose the signal
raw_signal = DC + sin1+sin2

#add noise to the Signal
noise = np.random.normal(mu, sigma, N)

#compose the recieved signal as the Signal plus Noise
SignalWithNoise = noise + raw_signal

#print the Signal to Noise ratio

Known_SNR = RMS(raw_signal)/RMS(noise)
print(f'Known SNR is {Known_SNR}')
Recieved_SNR = RMS(SignalWithNoise)/RMS(SignalWithNoise - raw_signal)
print(f'SNR of the recieved signal is {Recieved_SNR}')

########################################
##########Do some Filtering#############
########################################

#first, check the Frequency spectrum
numpyFourierSeries = np.fft.fft(SignalWithNoise)
'''plt.plot(numpyFourierSeries.real)
plt.xlabel("x")
plt.ylabel('magnitude')
plt.title('Numpy FFT')
plt.show()

plt.plot(numpyFourierSeries.imag)
plt.xlabel("x")
plt.ylabel('Phase')
plt.title('Numpy FFT')
plt.show()'''

#Put a Lowpass filter on the signal at the Nyquist frequency (150Hz)
lowpass_coef = signal.firwin(11, #number of taps, aka filter order
                   cutoff=149, #desired filter frequency
                   fs=SamplingRate,
                   pass_zero=True)
lowpass_data = signal.lfilter(lowpass_coef,[1.0],SignalWithNoise)


#Apply a Highpass filter to get rid of the DC componenst
highpass_coef = signal.firwin(11, #number of taps, aka filter order
                   cutoff=1, #desired filter frequency
                   fs=SamplingRate,
                   pass_zero=False)
filtered_data = signal.lfilter(highpass_coef,[1.0],lowpass_data)

#try to calculate the Signal to Noise Ratio
Recieved_SNR = RMS(filtered_data)/RMS(filtered_data - raw_signal)
print(f'SNR of the filtered signal is {Recieved_SNR}')

#i think i Fundamentall Don't understand how SNR is calculated
''' --I don't understand the Signal to noise characteristics here
From Signa = 0.1
Known SNR is                  10.28225806101168
SNR of the recieved signal is 10.344979933390572
SNR of the filtered signal is 00.9411789775640099'''



'''plt.plot(SignalWithNoise)
plt.xlabel("x")
plt.ylabel('magnitude')
plt.title('Signal with Noise')
plt.show()

plt.plot(filtered_data)
plt.xlabel("x")
plt.ylabel('Y')
plt.title('Filtered Data')
plt.show()

numpyFourierSeries = np.fft.fft(filtered_data)
plt.plot(numpyFourierSeries.real)
plt.xlabel("x")
plt.ylabel('magnitude')
plt.title('Numpy FFT')
plt.show()

plt.plot(numpyFourierSeries.imag)
plt.xlabel("x")
plt.ylabel('Phase')
plt.title('Numpy FFT')
plt.show()'''

