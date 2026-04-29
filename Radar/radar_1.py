#Zach Nelson
#generate a pulsed signal 

import numpy as np
import math
import matplotlib.pylab as plt

T = 1  #length of the recording in seconds
SamplingRate = 100 * 10*6 #10 M Hz 
N = T*SamplingRate #total number of samples
P = 10*10**(-2)

index = np.arange(N)    #counts 1,2,3 ..
timestep = index/SamplingRate #counts up to 10 by 1/300


#signal Parameters
W1 = 1000 #Hz
pi = math.pi

#generate a pulsed signal with length 
DC = np.ones(N) * 0.25
square = np.concat( [np.ones(int(P*SamplingRate)), np.zeros(int((T-P)*SamplingRate))]   )
sin1 = np.sin(timestep*W1*(2*pi))
pulse = square * sin1


plt.plot(sin1)
plt.xlabel("x")
plt.ylabel('magnitude')
plt.title('Numpy FFT')
plt.show()
plt.plot(square)
plt.xlabel("x")
plt.ylabel('magnitude')
plt.title('Numpy FFT')
plt.show()
plt.plot(pulse)
plt.xlabel("x")
plt.ylabel('magnitude')
plt.title('Numpy FFT')
plt.show()


delay = 50*10**(-2)
#Detect the signal in noise
recieved_square = np.concat( [np.zeros(int(delay*SamplingRate)), np.ones(int(P*SamplingRate)), np.zeros(int((T-P-delay)*SamplingRate))]   )
bounce = recieved_square * np.sin(timestep*W1*(2*pi))*0.1


'''plt.plot(bounce)
plt.xlabel("x")
plt.ylabel('recieved Signal')
plt.title('recieved Signal')
plt.show()'''

#Noise in recieved signal
mu, sigma = 0, .1
noise = np.random.normal(mu, sigma, N)

bounce = bounce + noise*recieved_square 
'''plt.plot(bounce)
plt.xlabel("x")
plt.ylabel('recieved Signal')
plt.title('recieved Signal')
plt.show()'''

#background noise
mu, sigma = 0, .3
noise = np.random.normal(mu, sigma, N)

Recieved_Signal = bounce + noise
plt.plot(Recieved_Signal)
plt.xlabel("x")
plt.ylabel('recieved Signal')
plt.title('recieved Signal')
plt.show()


#apply a matched filter:
#######################

#use a signal template:
#pulse is the template

correlation = np.zeros(int(T*SamplingRate))
template = np.ones(int(P*SamplingRate)) * np.sin(timestep[0:int(P*SamplingRate)]*W1*(2*pi))
prepend = np.zeros(0)
postpend = np.zeros(int((T-P)*SamplingRate))

for i in range(int(len(correlation)-P*SamplingRate)):
    #calculate the correlation
    T = np.concat([prepend,template,postpend])
    corr = np.sum(T*Recieved_Signal)
    correlation[i] = correlation[i] + corr

    #move the template one forward
    prepend = np.concat([prepend, np.zeros(1)])
    postpend = postpend[0:-1]

plt.plot(correlation)
plt.xlabel("x")
plt.title('matched Filter output')
plt.ylabel('corelation')
plt.show()