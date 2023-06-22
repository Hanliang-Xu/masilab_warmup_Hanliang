#################################################################
# The data_dir variable is the only input allowed to your code. 
# Do not modify any file names in the image directory.

data_dir = "./MASI_pets"
# Add your code below.
#################################################################

import os
import PIL
from PIL import Image
import numpy as np
import cv2

file_name = os.listdir(data_dir)
width = []
height = []
dim = []
size = []
ratio = []
pet_name = []
owner_name = []

for i in range(len(file_name)) :
    
    file_path = data_dir + "/" + file_name[i]
    im = cv2.imread(file_path)
    dim.append(im.shape)
    size.append(im.shape[0] * im.shape[1])
    ratio.append(im.shape[0] * 1.0 / im.shape[1])
    name_separated = file_name[i].split(".")[0]
    pet_name.append(name_separated.split("_")[0])
    owner_name.append(name_separated.split("_")[1])
    print(owner_name[i])