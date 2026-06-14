# Zach Nelson

#read the raw data.csv file and do stuff to it

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks, find_peaks_cwt
#TRy USing PyWavelets
import pywt 

data_file = r'/home/zach/Code/personal/Acceleration without g/Raw Data.csv'

dataframe = pd.read_csv(data_file)

# File has a header:
#"Time (s)","Linear Acceleration x (m/s^2)","Linear Acceleration y (m/s^2)","Linear Acceleration z (m/s^2)","Absolute acceleration (m/s^2)"

##Plot using:
dataframe.plot(x='Time (s)', y='Linear Acceleration z (m/s^2)')
plt.show()

time = dataframe['Time (s)'].to_numpy()


x = dataframe['Linear Acceleration x (m/s^2)'].to_numpy()
y = dataframe['Linear Acceleration y (m/s^2)'].to_numpy()
z = dataframe['Linear Acceleration z (m/s^2)'].to_numpy()

dt = (time[1]-time[0])

print(f'T = {dt}')
print(f'Fs = {1/dt}')
print(f'Fn = {(1/(2*dt))}')


#plt.plot(time, z)
#plt.show()
#coeficients
#cA, cD = pywt.dwt(z, 'db1')





'''# calcualte the fourier transform
fft_values = fft(z)
frequencies = fftfreq(len(time), dt)

plt.plot(frequencies, np.abs(fft_values))
plt.title('Fourier Transform (Frequency Domain)')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()

'''


'''
scale = 16


#Next,, show the Waveley transform
#f = scale2frequency('morlet', scale)/dt
scales = np.logspace(np.log10(1), np.log10(scale), scale)
# performe continuous wavelet transform using the Morlet wavelet
coefficients, frequecies = pywt.cwt(z, scales, wavelet='mexh')


plt.imshow(
    np.abs(coefficients),
    extent=[time[0], time[-1], scales[-1], scales[0]],  # actual time range
    cmap='PRGn',
    aspect='auto',
    vmax=np.abs(coefficients).max(),
    vmin=-np.abs(coefficients).max()
)
plt.show()'''

#cwt_peaks, _ = find_peaks(coeficients)

#this is actually pretty good at finding peaks
t_peaks, _ = find_peaks(z, height=0.2, distance=0.4/dt)
plt.plot(z)
plt.plot(t_peaks, z[t_peaks], "x")
plt.show()

Mean_HR = np.diff(t_peaks).mean() * dt
print(f'Mean time between heart beats is: {Mean_HR}')
print(f'Heart Rate: {60/Mean_HR}')


#try using peaks
cwt_peaks = find_peaks_cwt(z, #Data
                           widths=np.arange(1,200) #using a pulse width of 200 samplles, that looks about right
                            )
hr_est_cwt = np.diff(cwt_peaks).mean() * dt
print(f'Mean time between heart beats is: {hr_est_cwt}')
print(f'Heart Rate: {60/hr_est_cwt}')



