import matplotlib.pyplot as plt
import json
import cv2
import os

# [Resize images]
# Resize the image to 1024x1024
#
# 1. images_fold_path:  the folder includes image you want to resize
# ex: images_fold_path = 'detection/images/face'

images_fold_path = 'detection/images/face'
# select the jpg files
files = os.listdir(images_fold_path)

for file in files:

    file = os.path.join(images_fold_path, file)
    image = cv2.imread(file)
    image = cv2.resize(image, (1024,1024), interpolation=cv2.INTER_AREA)
    cv2.imwrite(file, image)