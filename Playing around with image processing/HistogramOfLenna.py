#Zach Nelson
#May 22
#Generate a Histogram of Lenna across each of the three colors

import numpy as np
import cv2

lenna = cv2.imread('Lenna_(test_image).png')


lenna_Red = lenna[:,:,0]
cv2.imshow('red', lenna_Red)

lenna_Green = lenna[:,:,1]
cv2.imshow('green', lenna_Green)

lenna_Blue = lenna[:,:,2]
cv2.imshow('Blue', lenna_Blue)





#Code needed to be included otherwise cv2 won't show the image
cv2.waitKey(0)
cv2.destroyAllWindows()