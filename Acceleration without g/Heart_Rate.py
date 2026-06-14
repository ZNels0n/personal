# Zach Nelson

#read the raw data.csv file and do stuff to it

#basic imports for data processing and vis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Signal Processing
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks, find_peaks_cwt

#PyWavelets
import pywt 

#Grab the data
# Note: CSV Header looks like:
#"Time (s)","Linear Acceleration x (m/s^2)","Linear Acceleration y (m/s^2)","Linear Acceleration z (m/s^2)","Absolute acceleration (m/s^2)"
data_file = r'/home/zach/Code/personal/Acceleration without g/Raw Data.csv'
dataframe = pd.read_csv(data_file)

#PLot the Raw Data
dataframe.plot(x='Time (s)', y='Linear Acceleration z (m/s^2)', title="Raw Time-Series Data")
plt.show()




#grab the data and put it into a numpy (np format)
time = dataframe['Time (s)'].to_numpy()
x = dataframe['Linear Acceleration x (m/s^2)'].to_numpy()
y = dataframe['Linear Acceleration y (m/s^2)'].to_numpy()
z = dataframe['Linear Acceleration z (m/s^2)'].to_numpy()

#Get the Sample Time and Sample Rate
T = (time[1]-time[0]) 
Fs = 1/T

print(f'T = {T}')
print(f'Fs = {Fs}')
print(f'Fn = {(Fs/2)}') #Nyquist frequency


# calcualte the fourier transform
fft_values = fft(z)
frequencies = fftfreq(len(time), T)


plt.plot(frequencies, np.abs(fft_values))
plt.title('Fourier Transform (Frequency Domain)')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()



scale = 16

#Next,, show the Wavelet transform
scales = np.logspace(np.log10(1), np.log10(scale), scale)
# performe continuous wavelet transform using the MExican Hat Wavelet
coefficients, frequecies = pywt.cwt(z, scales, wavelet='mexh')

plt.imshow(
    np.abs(coefficients),
    extent=[time[0], time[-1], scales[-1], scales[0]],  # actual time range
    cmap='PRGn',
    aspect='auto',
    vmax=np.abs(coefficients).max(),
    vmin=-np.abs(coefficients).max()
)
plt.show()




#Find the peaks With enough promencance. These are individual Heartbeats
#I tried two methods here from scipy, find_peaks and find_peaks_cwt



#Using find_peaks. this is the time domain version. 
t_peaks, _ = find_peaks(z, height=0.2, distance=0.4/T)
plt.plot(z)
plt.plot(t_peaks, z[t_peaks], "x")
plt.title('Finding Peaks using time Domain representation')
plt.show()

Mean_HR = np.diff(t_peaks).mean() * T
print(f'Mean time between heart beats is: {Mean_HR}')
print(f'Heart Rate: {60/Mean_HR}')


#Find Peaks using the Continious wavelet transoform
cwt_peaks = find_peaks_cwt(z, #Data
                           wiThs=np.arange(1,200) #using a pulse wiTh of 200 samplles, that looks about right
                            )
hr_est_cwt = np.diff(cwt_peaks).mean() * T
print(f'Mean time between heart beats is: {hr_est_cwt}')
print(f'Heart Rate: {60/hr_est_cwt}')



