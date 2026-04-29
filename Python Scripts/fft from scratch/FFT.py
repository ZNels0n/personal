'''
This file contains functions to compute the Fast Fourier Transform 

This is my attempt at coding the FFT algorithm from scratch 
basing this on the Fast Fourier Transform Wikipedia page

'''

import numpy as np
import math
from sys import exit
import matplotlib.pylab as plt

def FastSin(x, n):
    '''uses the tailor expansion for the sin function to n many terms'''
    sum = 0
    sign = 1
    for i in range(1,n+1,2):
        sum = sum + sign * math.pow(x, i)/math.factorial(n)
        sign = -sign
    return sum

def FastCos(x, n):
    '''uses the tailor expansion for the Cos function to n many terms'''
    sum = 0
    sign = 1
    for i in range(0,n+1,2):
        sum = sum + sign*math.pow(x, i)/math.factorial(n) 
        sign = -sign
    return sum

def FastFourierTransform():
    print("I want to calculate the FFT for this data")

def DiscreteFourierTransform(sequence, tailor_precision = 3):
    print("I want to compute the Discrete Fourier Transform on this data")
    '''The discrete Fourier Transform transforms a sequence of N floats into another sequence of floats which are the coeficients of the fourier representation of the signal
    X_n = Sum[0,N-1] xn * e^ (-i*2pi(k/N)*n)
    where xn is the input point
    X_n is the output point
    N is the number of points in the time series
    n is the point in the Frequency domain
    k is the point in the time domain
    
    we can rearrange this to be
    e^ix = cos(x) + i*sin(x)
    Magnitude of e^ix is the magnitude of the frequency component at n
    phase of e^ix is the Phase shift of this component

    '''
    N = sequence.shape[0]
    FourierSequence = np.zeros((2,N)) #shape is a touple
    for nf in range(N):
        #sum up across the elements in the time sequnce
        realf_n = 0
        imagf_n = 0
        #compute the e^ix for this element in the sequence
        for kt in range(N):
            #grab this point in the time series
            xt_n = sequence[kt]
            #compute x
            x = 2*math.pi*(kt/N)*nf
            #real = FastCos(x,tailor_precision)
            real = xt_n* math.cos(x)

            #imag = FastSin(x,tailor_precision)
            imag = xt_n* math.sin(x)
            realf_n = realf_n + real
            imagf_n = imagf_n - imag

        magf_n = math.sqrt(pow(realf_n,2) + pow(imagf_n,2))
        phasef_n = math.atan(imagf_n/realf_n) if realf_n != 0 else 0
        FourierSequence[0,nf] = magf_n
        FourierSequence[1,nf] = phasef_n
    print("I am done calculating the fourier transfrom on this data")
    return FourierSequence

def plot_shifted_fourier(Fseries): #, Fs):
    #because the Fourier Series outputs values in Ascending dF, then increasing negative df
    #You have to shift the series to get a good plot
    toPlot = Fseries #since my Fourier Sequence outputs in two rows? (rows or cols?)
    
    L = len(Fseries[0])
    
    
    H = int(L/2)
    neg_freqs = toPlot[:, H-1:-1].copy()
    pos_freqs = toPlot[:, 0:H].copy()
    toPlot = np.concatenate((neg_freqs,pos_freqs), axis=1)

    #indices = np.ones(-H,H)

    plt.plot(np.log10(toPlot[0,:]))
    plt.xlabel("x")
    plt.ylabel('magnitude')
    plt.title('Numpy FFT')
    plt.show()

    plt.plot(toPlot[1,:])
    plt.xlabel("x")
    plt.ylabel('Phase')
    plt.title('Numpy FFT')
    plt.show()


def Cooley_Tukey():
    print("computing the Cooley-Tukey FFT")
    ''''''