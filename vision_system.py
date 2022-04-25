from skimage.util import img_as_float
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import cv2

import image_manip
import imageSeg

class vision_system:
    def __init__(self):
        self.goodImage = None
        self.inputImage = None
        self.goodLogo = image_manip.logo()
        self.inputLogo = image_manip.logo()
        self.feature_vec_manager = image_manip.feature_vector_manager()
        self.threshold = 5   # mangage threshold for feature detection

        self.goodMask  = None
        self.inputMask = None

    # manage good logo
    def set_good_image(self, image_path):
        self.goodLogo.original_image = img_as_float(io.imread(image_path))
        self.goodImage = cv2.imread(image_path)
    
    def isolate_good_image_logo(self):
        self.goodLogo.isolated_logo, self.goodMask = imageSeg.image_segmentation(self.goodLogo.original_image)

    def get_good_image_features(self):
        fig = plt.figure("Superpixels segments" )
        ax = fig.add_subplot(1, 1, 1)
        ax.imshow(self.goodLogo.isolated_logo)
        plt.axis("off")
        plt.savefig("out.jpg", transparent=True, bbox_inches='tight', pad_inches=-0.1)
        # image_fi = open("out.jpg", "rb")

        # self.feature_vec_manager.set_image(image_fi.read())
        self.goodLogo.feature_vector = self.feature_vec_manager.get_feature_vector()

    # manage input logo
    def set_input_image(self, image_path):
        self.inputLogo.original_image = img_as_float(io.imread(image_path))
        self.inputImage = cv2.imread(image_path)
    
    def isolate_input_image_logo(self):
        self.inputLogo.isolated_logo, self.inputMask = imageSeg.image_segmentation(self.inputLogo.original_image)

    def get_input_image_features(self):
        fig = plt.figure("Superpixels segments" )
        ax = fig.add_subplot(1, 1, 1)
        ax.imshow(self.inputLogo.isolated_logo)
        plt.axis("off")
        plt.savefig("out.jpg", transparent=True, bbox_inches='tight', pad_inches=-0.1)
        # image_fi = open("out.jpg", "rb")

        # self.feature_vec_manager.set_image(image_fi.read())
        self.inputLogo.feature_vector = self.feature_vec_manager.get_feature_vector()
    
    def brightness_difference(self, mask1, mask2):
        gray1 = cv2.cvtColor(self.goodImage, cv2.COLOR_RGB2GRAY)
        gray2 = cv2.cvtColor(self.inputImage, cv2.COLOR_RGB2GRAY)
        h1 = cv2.calcHist([gray1], [0], mask1, [256], [0.0,255.0])
        h2 = cv2.calcHist([gray2], [0], mask2, [256], [0.0,255.0])
        return cv2.compareHist(h1,h2,method=cv2.HISTCMP_BHATTACHARYYA)

    def match(self):
        check1 = self.feature_vec_manager.match(self.goodLogo.feature_vector, self.inputLogo.feature_vector)# < 8
        check2 = 0.05 < self.brightness_difference(self.goodMask, self.inputMask) < 0.08# < 0.01
        return (check1, check2)


