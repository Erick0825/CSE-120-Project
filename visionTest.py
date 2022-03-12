from base64 import b64encode
import json
import requests
import numpy as np

latent_vector1 = []
latent_vector2 = []

# using api from latentvector.space to get
# feature vector for an image from the resnet18 model
# trained on ImageNet dataset
url = "https://sruhyjfrd6.execute-api.us-east-2.amazonaws.com/image"

with open("random.jpeg", "rb") as imageFile:
    img_string = b64encode(imageFile.read()).decode('utf-8')

data = {"image": img_string}
req = requests.post(url, json=data)

if req.status_code == 200:
    # Get latent vector
    latent_vector1 = req.json()['body']['image_vector']

else:
    print(req.json()) # failed to get feature vector


with open("random.jpeg", "rb") as imageFile:
    img_string = b64encode(imageFile.read()).decode('utf-8')

data = {"image": img_string}
req = requests.post(url, json=data)

if req.status_code == 200:
    # Get latent vector
    latent_vector2 = req.json()['body']['image_vector']

else:
    print(req.json()) # failed to get feature vector

b = np.array(latent_vector2)
a = np.array(latent_vector1)

dist = np.sqrt(np.sum(np.square(a-b)))
print(dist)