from base64 import b64encode
import numpy as np
import model
from scipy import spatial


class logo:
    original_image = []
    isolated_logo = []
    feature_vector = []

class feature_vector_manager:
    # feature vector for an image from the resnet152 model
    # trained on ImageNet dataset
        
    def get_feature_vector(self, image_path):
        return model.get_vector(image_path)

    # compute similarity between two feature vectors
    def match(self, a, b):
        # return 1 - spatial.distance.cosine(a, b)
        return np.sqrt(np.sum(np.square(a-b)))