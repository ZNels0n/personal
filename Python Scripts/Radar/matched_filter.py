#zach Nelson
#funciton which computes the matched filter output for the signal

import numpy as np
from math import pi, log
import matplotlib.pylab as plt

def matched_filter(template, recieved_signal):
    correlation = np.zeros(int(len(recieved_signal)-len(template)))
    prepend = np.zeros(0)
    postpend = np.zeros(int((len(recieved_signal)-len(template))))

    for i in range(len(correlation)):
        #calculate the correlation
        T = np.concat([prepend,template,postpend])
        corr = np.sum(T*recieved_signal)
        correlation[i] = correlation[i] + corr

        #move the template one forward
        prepend = np.concat([prepend, np.zeros(1)])
        postpend = postpend[0:-1]
    return correlation

def matched_filter_conv(template,recieved_signal):
    h = np.conj(template[::-1])
    #return np.convolve(h, recieved_signal, mode='valid')
    return np.convolve(recieved_signal,h , mode='valid')