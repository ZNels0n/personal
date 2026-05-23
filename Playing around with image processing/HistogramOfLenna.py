#Zach Nelson
#May 22
#Generate a Histogram of Lenna across each of the three colors

import numpy as np
import cv2
import matplotlib.pyplot as plt

lenna = cv2.imread('Lenna_(test_image).png')


lenna_Red = lenna[:,:,0]
#cv2.imshow('red', lenna_Red)
Red = lenna_Red.flatten()

lenna_Green = lenna[:,:,1]
#cv2.imshow('green', lenna_Green)
Green = lenna_Green.flatten()

lenna_Blue = lenna[:,:,2]
#cv2.imshow('Blue', lenna_Blue)
Blue = lenna_Blue.flatten()


#Red Histogram
Red_Hist, Red_Bins = np.histogram(Red)

#Green Histogram
Green_Hist, Green_Bins = np.histogram(Green)

#Blue Histogram
Blue_Hist, Blue_Bins = np.histogram(Blue)

plt.subplot(1,3,1)
plt.title('Red Histogram')
plt.plot(Red_Hist)

plt.subplot(1,3,2)
plt.title('Green Histogram')
plt.plot(Green_Hist)

plt.subplot(1,3,3)
plt.title('Blue Histogram')
plt.plot(Blue_Hist)

plt.show()



intensity = np.sqrt(Red_Hist*Red_Hist + Blue_Hist*Blue_Hist + Green_Hist*Green_Hist)

plt.plot(intensity)
plt.show()


#Code needed to be included otherwise cv2 won't show the image
cv2.waitKey(0)
cv2.destroyAllWindows()