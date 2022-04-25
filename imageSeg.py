# import the necessary packages
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io
import matplotlib.pyplot as plt
import numpy as np

def image_segmentation(image):
    #  get image
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-i", "--image", required = True, help = "Path to the image")
    # args = vars(ap.parse_args())

    # # cast image 
    # image = img_as_float(io.imread(args["image"]))
    image = image[:,:,:3]

    # set max number of segments
    numSegments = 3
    segments = slic(image, n_segments = numSegments, sigma = 14)

    # isolate image based on the middle segment
    # fig = plt.figure("Superpixels -- %d segments"%(numSegments))
    # ax = fig.add_subplot(1, 1, 1) 
    # ax.imshow(mark_boundaries(image, segments))
    image[segments!=2] = 0 # isolate to only the 2nd segment

    # crop image to only the 2nd segment
    left = len(segments[0])
    right = 0
    up = len(segments)
    bottom = 0
    for i in range(len(segments)):
        for j in range(len(segments[0])):
            if segments[i][j] == 2:
                bottom = i
                if i < up:
                    up = i
                if j > right:
                    right = j
                if j < left:
                    left = j
    image2 = []
    for i in range(len(segments)):
        image2.append(image[i][left:right+1])
    image2 = image2[:bottom]
    image2 = image2[up:]

    segments[segments!=2] = 0
    segments[segments!=0] = 255

    # for i in range(len(segments)):
    #     for j in range(len(segments[i])):
    #         if segments[i][j] != 2:
    #             segments[i][j] = 0
    #         else:
    #             segments[i][j] = 1
    #         image[i][j] *= segments[i][j]
    # ax.imshow(image)
    # plt.axis("off") 
    # plt.show()
    # # save image
    # plt.savefig("out.jpg", transparent=True, bbox_inches='tight', pad_inches=-0.1)

    return image2, np.asarray(segments, dtype="uint8")

