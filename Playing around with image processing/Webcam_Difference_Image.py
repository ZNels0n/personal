#Zach Nelson
#
#script which reads in webcam footage
#greyscales the incoming feed
#creates the difference image Frame_i - Frame_(i-1)
#displays

#imports

import cv2
import numpy as np
import sys


camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print('no camera, exiting')
    sys.exit()

ret,frame = camera.read()
lastFrame = frame
#ave = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
ave = np.float32(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))


while True:
    #read in the webcam image
    ret,frame = camera.read()

    cv2.imshow('raw frame',frame)

    #should probably greyscale the image?
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    last_grey_image = cv2.cvtColor(lastFrame, cv2.COLOR_BGR2GRAY)

    cv2.accumulateWeighted(gray_image, ave, .05)

    #take the difference between this frame and the last
    difference_image = cv2.absdiff(gray_image, last_grey_image)
    #show the difference image
    cv2.imshow('Difference_image',difference_image)

    #take a moving average, and remove the average from this frame. should remove the background?
    
    ave_uint8 = cv2.convertScaleAbs(ave)
    difference_image = cv2.absdiff(gray_image, ave_uint8)
    
    
    cv2.imshow('Running Average',ave_uint8)
    cv2.imshow('Frame minus Running Average',difference_image)
    #once we've show the image, move this frame to the next
    lastFrame = frame

    #let the q key break out of the loop
    if cv2.waitKey(1) == ord('q'):
        break

#clean everything up
camera.release()
cv2.destroyAllWindows()
