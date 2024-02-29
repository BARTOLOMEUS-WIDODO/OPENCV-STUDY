import numpy as np
import cv2 as cv

img = cv.imread(r'C:\Users\priyo\Desktop\python_cv1\Faces\val\elton_john\1.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

cv.imshow('Detected Face', img)

cv.waitKey(0)
