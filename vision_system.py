from skimage.util import img_as_float
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import cv2
import numpy as np

import image_manip

class vision_system:
    def __init__(self):
        self.templateLogo = image_manip.logo()
        self.inputLogo = image_manip.logo()
        self.feature_vec_manager = image_manip.feature_vector_manager()
        self.method = eval('cv2.TM_CCOEFF')

    # manage good logo
    def set_good_image(self, image_path):
        self.templateLogo.original_image = cv2.imread(image_path, 0)
        self.w, self.h = self.templateLogo.original_image.shape[::-1]
        
        self.templateLogo.feature_vector = self.feature_vec_manager.get_feature_vector(image_path)
        self.gray1 = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_RGB2GRAY)

    # manage input logo
    def set_input_image(self, image_path):
        self.inputLogo.original_image = cv2.imread(image_path, 0)

        # Apply template Matching and crop image down
        res = cv2.matchTemplate(self.inputLogo.original_image, self.templateLogo.original_image, self.method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + self.w, top_left[1] + self.h)
        crop_img = self.inputLogo.original_image [top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
        cv2.imwrite("out.jpg", crop_img)

        self.template_match = max_val

        self.inputLogo.feature_vector = self.feature_vec_manager.get_feature_vector("out.jpg")

        self.gray2 = cv2.cvtColor(cv2.imread("out.jpg"), cv2.COLOR_RGB2GRAY)

    def brightness_difference(self):
        h1 = cv2.calcHist([self.gray1], [0], None, [256], [0.0,255.0])
        h2 = cv2.calcHist([self.gray2], [0], None, [256], [0.0,255.0])
        return cv2.compareHist(h1,h2,method=cv2.HISTCMP_BHATTACHARYYA)
        # distance = 0
        # for i in range(len(self.gray1)):
        #     for j in range(len(self.gray1)):
        #         distance += pow((self.gray1[i][j]-self.gray2[i][j]),2)
        # distance = np.sqrt(distance)
        # return distance

    def match(self):
        check1 = self.feature_vec_manager.match(self.templateLogo.feature_vector, self.inputLogo.feature_vector)

        # check1 =  self.brightness_difference()
        # check1 = self.template_match
        return check1


