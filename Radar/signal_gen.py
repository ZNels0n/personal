#resource function for generating a pulse sine 
import numpy as np
from math import pi, log
import matplotlib.pylab as plt

def square(on_time, sample_rate, off_time=0, delay=0,): #return a square wave
    return np.concat( [np.zeros(int(delay*sample_rate)), np.ones(int(on_time*sample_rate)), np.zeros(int(off_time*sample_rate))]   )

def sin_pulse(on_time, freq, sample_rate, off_time=0, delay=0, phase=0):
    timestep = np.arange(on_time*sample_rate)/sample_rate
    signal = np.sin(timestep*freq*(2*pi) + phase)
    pulse = np.concat( [np.zeros(int(delay*sample_rate)), signal, np.zeros(int(off_time*sample_rate))]   )
    return pulse

def chirp(on_time, freq_start, freq_end, sample_rate, off_time=0, delay=0, phase=0, Type='linear'):
    #a chirp is a sinusoidal pulse with increasing frequency
    
    timestep = np.arange(on_time*sample_rate)/sample_rate
    #this is the time domain expression for a chirp:
    #see https://en.wikipedia.org/wiki/Chirp for more info
    #in short, the instantanious phase is the integral of the frequency over time
    #in this implementation, the phase term acts like a DC offset of the phase over timeS
    
    match Type.lower():
        case 'linear':
            m=(freq_end-freq_start) / on_time
            signal = np.sin(2*pi*(0.5*m*timestep**2 + freq_start*timestep) + phase)

        case 'exponential':
            k = freq_end/freq_start
            phase_t = (1/log(k)) * on_time* (k**(timestep/on_time) - 1)
            signal = np.sin(2*pi*freq_start*phase_t + phase)

    pulse = np.concat( [np.zeros(int(delay*sample_rate)), signal, np.zeros(int(off_time*sample_rate))]   )
    return pulse


'''#example of chirp
birdy = chirp(on_time=1, freq_start=5, freq_end=20, sample_rate=10000, Type='linear')
plt.plot(birdy)
plt.xlabel("x")
plt.title('chirp')
plt.show()'''