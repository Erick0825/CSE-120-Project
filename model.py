import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from torch.autograd import Variable
from PIL import Image
import numpy as np


# prepare resnet50 model
model = models.resnet152(pretrained=True)
layer = model._modules.get('avgpool')
model.eval()

scaler = transforms.Resize((224, 224))
normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
to_tensor = transforms.ToTensor()


def get_vector(image_name):
    img = Image.open(image_name).convert('RGB')
    t_img = Variable(normalize(to_tensor(scaler(img))).unsqueeze(0))

    vec = torch.zeros(2048)
    # function copies output of a layer
    def copy_data(m, i, o):
        vec.copy_(o.data.reshape(o.data.size(1)))

    h = layer.register_forward_hook(copy_data)
    
    model(t_img)
    h.remove()
    return vec.numpy()

# a = get_vector("test3.png")
# b = get_vector("test1.png")
# print(np.sqrt(np.sum(np.square(a-b))))