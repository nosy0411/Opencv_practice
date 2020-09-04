import numpy as np
import cv2

img = cv2.imread('images/hallstatt.jpg')
px = img[340, 200]
print(px)

B = img.item(340, 200, 0)
G = img.item(340, 200, 1)
R = img.item(340, 200, 2)

BGR = [B, G, R]
print(BGR)

img.itemset((340, 200, 0), 100)

print(img.shape)
print(img.size)
print(img.dtype)



