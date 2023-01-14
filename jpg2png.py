import matplotlib.pyplot as plt
import json
import cv2
import os

# [Jpg to png]
# Change the jpg to png by designating the folder path
#
# 1. images_fold_path:  the folder includes image you want change jpg to png
# ex: images_fold_path = 'detection/images/face'


images_fold_path = r'C:\\Users\\AlexKuo\\Downloads\\Facemask'
# select the jpg files
files = os.listdir(images_fold_path) 
judge_jpg = lambda path: path.split('.')[-1] == 'jpg' #jpg or JPG
files = [file for file in files if judge_jpg(file)]

for file in files:
  print('process:',file)
  new_file_name = file.split(".")[0]
  file = os.path.join(images_fold_path, file)
  image = cv2.imread(file)
  cv2.imwrite(f'{images_fold_path}/{new_file_name}.png',image)
  os.remove(file)