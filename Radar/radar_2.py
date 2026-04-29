from signal_gen import *
from matched_filter import *
from sys import exit

T = 1  #length of the recording in seconds
SamplingRate = 1000 * 10**3 #10 M Hz 
N = T*SamplingRate #total number of samples
P = 10*10**(-2) #pulse length in seconds

index = np.arange(N)    #counts 1,2,3 ..
timestep = index/SamplingRate #counts up to 10 by 1/300


#signal Parameters
W1 = 200 #Hz
B = 398 #bandwidth


template1 = sin_pulse(on_time=P, freq=W1, sample_rate=SamplingRate)
template2 = chirp(on_time=P, freq_start=(W1+B/2), freq_end=(W1-B/2), sample_rate=SamplingRate, Type='linear')
template3 = chirp(on_time=P, freq_start=(W1+B/2), freq_end=(W1-B/2), sample_rate=SamplingRate, Type='exponential')

energy = np.sum(np.abs(template1)**2)
print(f'energy CW {energy}')
energy = np.sum(np.abs(template2)**2)
print(f'energy linear chirp {energy}')
energy = np.sum(np.abs(template3)**2)
print(f'energy exp chirp {energy}')


'''plt.subplot(3,1,1)
plt.plot(template1)
plt.subplot(3,1,2)
plt.plot(template2)
plt.subplot(3,1,3)
plt.plot(template3)
#plt.title('sent signalT')
plt.show()'''


#generate a pulsed signal with length 
#(on_time, freq, sample_rate, off_time=0, delay=0, phase=0):
pulse1 = sin_pulse(on_time=P, freq=W1, sample_rate=SamplingRate, off_time=(T-P))
pulse2 = chirp(on_time=P, freq_start=(W1+B/2), freq_end=(W1-B/2), sample_rate=SamplingRate,off_time=(T-P), Type='linear')
pulse3 = chirp(on_time=P, freq_start=(W1+B/2), freq_end=(W1-B/2), sample_rate=SamplingRate,off_time=(T-P), Type='exponential')

'''plt.subplot(3,1,1)
plt.plot(pulse1)
plt.subplot(3,1,2)
plt.plot(pulse2)
plt.subplot(3,1,3)
plt.plot(pulse3)
#plt.title('sent signalT')
plt.show()'''


delay = 50*10**(-2)
attenuation = .01
#Detect the signal in noise
bounce1 = sin_pulse(on_time=P, freq=W1, sample_rate=SamplingRate, off_time=(T-P-delay), delay=delay) * attenuation
bounce2 = chirp(on_time=P, freq_start=(W1+B/2), freq_end=(W1-B/2), sample_rate=SamplingRate,off_time=(T-P-delay), delay=delay, Type='linear') * attenuation
bounce3 = chirp(on_time=P, freq_start=(W1+B/2), freq_end=(W1-B/2), sample_rate=SamplingRate,off_time=(T-P-delay), delay=delay, Type='exponential') * attenuation

'''plt.subplot(3,1,1)
plt.plot(bounce1)
plt.subplot(3,1,2)
plt.plot(bounce2)
plt.subplot(3,1,3)
plt.plot(bounce3)
#plt.title('recieved pulse')
plt.show()
'''

#background noise
mu, sigma = 0, 1
noise = np.random.normal(mu, sigma, N)

Recieved_Signal1 = bounce1 + noise
Recieved_Signal2 = bounce2 + noise
Recieved_Signal3 = bounce3 + noise

plt.subplot(3,1,1)
plt.plot(Recieved_Signal1)
plt.subplot(3,1,2)
plt.plot(Recieved_Signal2)
plt.subplot(3,1,3)
plt.plot(Recieved_Signal3)
#plt.title('recieved Signal')
plt.show()


#apply a matched filter:
#######################

#use a signal template:
#pulse is the template

'''filter_output1 = matched_filter(template1, Recieved_Signal1)
filter_output2 = matched_filter(template2, Recieved_Signal2)
filter_output3 = matched_filter(template3, Recieved_Signal3)

plt.subplot(3,1,1)
plt.plot(filter_output1)
plt.subplot(3,1,2)
plt.plot(filter_output2)
plt.subplot(3,1,3)
plt.plot(filter_output3)
#plt.title('recieved Signal')
plt.show()'''



filter_output1 = matched_filter_conv(template1, Recieved_Signal1)
filter_output2 = matched_filter_conv(template2, Recieved_Signal2)
filter_output3 = matched_filter_conv(template3, Recieved_Signal3)

plt.subplot(3,1,1)
plt.plot(filter_output1)
plt.subplot(3,1,2)
plt.plot(filter_output2)
plt.subplot(3,1,3)
plt.plot(filter_output3)
#plt.title('recieved Signal')
plt.show()

exit()