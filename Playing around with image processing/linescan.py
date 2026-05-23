#just something silly
#show the Lena Image
#but
#replace the bottom row of the image with the top line
#get a silly sinking effect

import numpy as np
import cv2

lenna = cv2.imread('Lenna_(test_image).png')

# 1. Create a named window with the 'WINDOW_NORMAL' flag
cv2.namedWindow("lenna", cv2.WINDOW_NORMAL)

# 2. Set the window property to full screen
cv2.setWindowProperty("lenna", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)



lenna_copy = lenna.copy()
while True:
    lenna_copy = np.roll(lenna_copy, shift=1, axis=0)
    lenna_copy = np.roll(lenna_copy, shift=2, axis=1)
    #lenna_copy = np.roll(lenna_copy, shift=1, axis=2)
    cv2.imshow('lenna',lenna_copy)

    #CV2 doesn't process the queue unless there's a waitkey, apperently
    if cv2.waitKey(60) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()