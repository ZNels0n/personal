#Noise and Averaging:
#use Lenna to demonstrate on an image the technique from EEG processing of Evoked response:
#
#an EEG signal has very poor signal to noise, so many instances of the brain response that we're interested in are averaged togetehr
#we assume the noise has the same distrobution, so averaging across many samples the noise will be averaged away, leaving just the signal portion. 

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
noise_power = 50

def display_numpy_as_image(array):
    image_to_display = Image.fromarray(array.astype(np.uint8))
    image_to_display.show()

def Average_across_Noisy_samples(frame,shape, NoiseStrength, NumberOfSamples):
    noise_generator = np.random.default_rng()

    #make 10 noisy images, store them
    noisy_samples = []
    for i in range(NumberOfSamples):
        #noise is distributed from -1 to 1
        noise = 2*(noise_generator.random(size=shape)-0.5) * NoiseStrength
        NoisyFrame = frame + noise
        NoisyFrame = np.clip(NoisyFrame, 0, 255)
        noisy_samples.append(NoisyFrame)
    noisy_array = np.array(noisy_samples)
    averaged_sample = np.mean(noisy_array, axis = 0)
    return averaged_sample

def MeanSquareError(original, distorted):
    error = (original - distorted)**2
    MSE = np.mean(error, axis=(0,1,2))
    return MSE


#load in the image of Lenna
lenna = Image.open('Lenna_(test_image).png')
oneFrame = np.asarray(lenna)
print(type(oneFrame))
lenna_shape = oneFrame.shape #im sure she has a very nice shape
print(lenna_shape)
pixel_max = np.max(oneFrame)
pixel_range = np.ptp(oneFrame)

'''print('displaying image without distortion')
display_numpy_as_image(oneFrame)
print('finished printing image 1')'''

#add noise to a few images, average them, and show that the distortion decreases when we average across more samples
num_samples = list(range(0,100))
ErrorTrendWithSamples = []
noise_strength = noise_power*pixel_max
for i in num_samples:
    sample =Average_across_Noisy_samples(oneFrame,lenna_shape, noise_strength, NumberOfSamples=i)
    MSE = MeanSquareError(oneFrame, sample)
    print(f'MSE of {i} samples is {MSE}')
    ErrorTrendWithSamples.append(MSE)
plt.plot(num_samples,ErrorTrendWithSamples)
plt.title('Error Trend With MSE vs number of Samples')
plt.show()


# for a fixed number of samples, increase the noise leveland show that the distortion increases even after averaging
noisepower_values = list(range(0,100, 1))
ErrorTrendWithNoisePower = []
for i in noisepower_values:
    noise_strength = 0.1*i*pixel_max
    sample = Average_across_Noisy_samples(oneFrame,lenna_shape, noise_strength, NumberOfSamples=10)
    MSE = MeanSquareError(oneFrame, sample)
    print(f'MSE of 10 sample average with NoisePower {i} is {MSE}')
    ErrorTrendWithNoisePower.append(MSE)
plt.plot(noisepower_values,ErrorTrendWithNoisePower)
plt.title('Error Trend with MSE vs Noise POwer for 10 averaged samples')
plt.show()

