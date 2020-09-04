import numpy as np
import cv2

img = cv2.imread('images/hallstatt.jpg')

b,g,r = cv2.split(img)

print(img[100, 100])
print(b[100, 100], g[100, 100], r[100, 100])

cv2.imshow('original', img)

subimg = img[300:400, 350:750]
cv2.imshow('cutting', subimg)

img[300:400, 0:400] = subimg

print(img.shape)
print(subimg.shape)

cv2.imshow('modified', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

