import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cv2
from PIL import Image, ImageDraw
from images2gif import writeGif

import glob

files = sorted(glob.glob('output/*.png'))
images = list(map(lambda file: Image.open(file), files))
images[0].save('out.gif', save_all=True, append_images=images[1:], duration=100, loop=0)    

"""
images = [Image.open(image) for image in glob.glob('output/*.png')]
file_path_name = '3d_test.gif'
writeGif(file_path_name, images, duration=0.1)
"""