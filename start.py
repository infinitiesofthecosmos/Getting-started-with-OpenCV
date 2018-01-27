# Getting-started-with-OpenCV
This repository includes some basic codes which exhibit the usage of openCV in Python.


import numpy as np
import cv2
img = cv2.imread('sample.jpg',0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
