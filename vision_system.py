from skimage.util import img_as_float
from skimage import io
import numpy as np
import matplotlib.pyplot as plt

import image_manip
import imageSeg

class vision_system:
    def __init__(self):
        self.goodLogo = image_manip.logo()
        self.inputLogo = image_manip.logo()
        self.feature_vec_manager = image_manip.feature_vector_manager()

    # manage good logo
    def set_good_image(self, image_path):
        self.goodLogo.original_image = img_as_float(io.imread(image_path))
    
    def isolate_good_image_logo(self):
        self.goodLogo.isolated_logo = imageSeg.image_segmentation(self.goodLogo.original_image)

    def get_good_image_features(self):
        fig = plt.figure("Superpixels segments" )
        ax = fig.add_subplot(1, 1, 1)
        ax.imshow(self.goodLogo.isolated_logo)
        plt.axis("off")
        plt.savefig("out.jpg", transparent=True, bbox_inches='tight', pad_inches=-0.1)
        # save and then open image to go around problem of 
        # the isolated_logo being in the type of floats
        # which is too big for api to handle
        image_fi = open("out.jpg", "rb")

        self.feature_vec_manager.set_image(image_fi.read())
        self.goodLogo.feature_vector = self.feature_vec_manager.get_feature_vector()

    # manage input logo
    def set_input_image(self, image_path):
        self.inputLogo.original_image = img_as_float(io.imread(image_path))
    
    def isolate_input_image_logo(self):
        self.inputLogo.isolated_logo = imageSeg.image_segmentation(self.inputLogo.original_image)

    def get_good_input_features(self):
        fig = plt.figure("Superpixels segments" )
        ax = fig.add_subplot(1, 1, 1)
        ax.imshow(self.inputLogo.isolated_logo)
        plt.axis("off")
        plt.savefig("out.jpg", transparent=True, bbox_inches='tight', pad_inches=-0.1)
        # save and then open image to go around problem of 
        # the isolated_logo being in the type of floats
        # which is too big for api to handle
        image_fi = open("out.jpg", "rb")

        self.feature_vec_manager.set_image(image_fi.read())
        self.inputLogo.feature_vector = self.feature_vec_manager.get_feature_vector()



