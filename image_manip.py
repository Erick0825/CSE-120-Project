from base64 import b64encode
import json
import requests
import numpy as np


class logo:
    original_image = []
    isolated_logo = []
    feature_vector = []

class feature_vector_manager:
    # using api from latentvector.space to get
    # feature vector for an image from the resnet18 model
    # trained on ImageNet dataset
    def __init__(self):
        self.feature_vector_api = "https://sruhyjfrd6.execute-api.us-east-2.amazonaws.com/image"
    
    # set an image
    def set_image(self, image_bytes):
        self.img_string = b64encode(image_bytes).decode('utf-8')
        self.data = {"image": self.img_string}

    # call api with the current image and return feature vector
    def get_feature_vector(self):
        req = requests.post(self.feature_vector_api, json=self.data)

        if req.status_code == 200:
            # Get latent vector
            f_vector = req.json()['body']['image_vector']
            return np.array(f_vector)
        else:
            print(req.json()) # failed to get feature vector
            return np.array([])


    # compute similarity between two feature vectors
    def match(self, a, b):
        return np.sqrt(np.sum(np.square(a-b)))