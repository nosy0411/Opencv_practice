import numpy as np
import cv2

img = cv2.imread('images/hallstatt.jpg')

b, g, r = cv2.split(img)

cv2.imshow('blue channel', b)
cv2.imshow('green channel', g)
cv2.imshow('red channel', r)

merged_img = cv2.merge((b,g,r))
cv2.imshow('merged', merged_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
