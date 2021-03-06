
import numpy as np
import matplotlib.pyplot as plt
from skimage.restoration import denoise_tv_chambolle

# Make sure that caffe is on the python path:
caffe_root = '../'  # this file is expected to be in {caffe_root}/examples
import sys
sys.path.insert(0, caffe_root + 'python')

import caffe

# Set the right path to your model definition file, pretrained model weights,
# and the image you would like to classify.
MODEL_FILE = '../models/bvlc_reference_caffenet/deploy.prototxt'
PRETRAINED = '../models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'
IMAGE_FILE = 'images/cat.jpg'

with open('../data/ilsvrc12/synset_words.txt') as f:
    content = f.readlines()



net = caffe.Classifier(MODEL_FILE, PRETRAINED,
                       mean=np.load(caffe_root + 'python/caffe/imagenet/ilsvrc_2012_mean.npy').mean(1).mean(1),
                       channel_swap=(2,1,0),
                       raw_scale=255,
                       image_dims=(256, 256))

input_image = caffe.io.load_image(IMAGE_FILE)
input_image = denoise_tv_chambolle(input_image, weight=0.2, multichannel=True)

prediction = net.predict([input_image])  # predict takes any number of images, and formats them for the Caffe net automatically
pclass = prediction[0].argmax()
print 'predicted class:', pclass, prediction[0][pclass]
print 'predicted class name:', content[pclass]

