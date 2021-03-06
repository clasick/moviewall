import numpy as np
from PIL import Image 
import os
import sys

list_im = []

try:
    USER = sys.argv[1]
except IndexError:
    print('Please enter the name of the user to retrieve the wallaper for!')
    print('Example: python image.py clasick')

for file in os.listdir(USER + '/'):
    if file.endswith('.jpg') and "wallpaper" not in file:
        print("Gathering image: {}".format(file))
        list_im.append(USER + '/'  + file)

list_im.sort(key=lambda x: os.stat(os.path.join('', x)).st_mtime)

imgs = [ Image.open(i) for i in list_im]

min_shape = (230,330)

horz = []

#wallpaper size for 1080p = 9width and 4 height

for x in range(0,36,9):
    nine = ()
    for y in range(x,x+9,1):
        if y <= len(imgs)-1:
            nine = nine + ((np.asarray(imgs[y].resize(min_shape))),)
    imgs_comb = np.hstack((image) for image in nine)
    horz.append(imgs_comb)

vert = np.vstack(line for line in horz)

imgs_comb = Image.fromarray(vert)

save_path = USER + '/wallpaper.jpg'

imgs_comb.save(USER + '/wallpaper.jpg')

if os.path.exists(save_path):
    print("File created at: {}".format(save_path))
