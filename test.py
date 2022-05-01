import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from torch.autograd import Variable
from PIL import Image
import numpy as np


method = eval('cv.TM_CCOEFF')


for spring_number in range(3, 4):
    template = cv.imread('images/Good_Images/Spring' + str(spring_number) + '_cropped.jpeg',0)
    w, h = template.shape[::-1]
    for i in range(1, 5):
        for bad_number in range(5):
            img = cv.imread('images/Bad_Images/Spring' + str(spring_number) + '_' + str(i) + '_bad' + str(bad_number) + '.jpeg',0)

            # Apply template Matching
            res = cv.matchTemplate(img,template,method)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)

            crop_img = img[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
            cv.imwrite("out.jpg", crop_img)

