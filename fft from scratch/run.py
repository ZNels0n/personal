

from FFT import *

#params
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
'''
plt.plot(raw_signal)
plt.xlabel("x")
plt.ylabel('seqence value')
plt.show()'''


MyFourierSeries = DiscreteFourierTransform(raw_signal)
numpyFourierSeries = np.fft.fft(raw_signal)

plot_shifted_fourier(MyFourierSeries)


