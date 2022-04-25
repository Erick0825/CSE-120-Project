from base64 import b64encode
import numpy as np
import model
from scipy import spatial


class logo:
    original_image = []
    isolated_logo = []
    feature_vector = []

class feature_vector_manager:
    # feature vector for an image from the resnet50 model
    # trained on ImageNet dataset
        
    # # set an image
    # def set_image(self, image_bytes):
    #     self.img_string = b64encode(image_bytes).decode('utf-8')
    #     self.data = {"image": self.img_string}

    # call api with the current image and return feature vector
    def get_feature_vector(self):
        return model.get_vector("out.jpg")

    # compute similarity between two feature vectors
    def match(self, a, b):
        # return 1 - spatial.distance.cosine(a, b)
        return np.sqrt(np.sum(np.square(a-b)))