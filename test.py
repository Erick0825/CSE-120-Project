import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


method = eval('cv.TM_CCOEFF')


for spring_number in range(3, 4):
    template = cv.imread('images/Good_Images/Spring' + str(spring_number) + '_cropped.jpeg',0)
    w, h = template.shape[::-1]
    for i in range(5):
        for bad_number in range(5):
            img = cv.imread('images/Bad_Images/Spring' + str(spring_number) + '_' + str(i) + '_bad' + str(bad_number) + '.jpeg',0)

            # Apply template Matching
            res = cv.matchTemplate(img,template,method)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv.rectangle(img,top_left, bottom_right, 255, 10)
            plt.subplot(121),plt.imshow(res,cmap = 'gray')
            plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
            plt.subplot(122),plt.imshow(img,cmap = 'gray')
            plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
            plt.show()