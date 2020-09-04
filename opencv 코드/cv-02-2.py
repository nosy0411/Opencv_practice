import numpy as np
import cv2

def showlmage():
    imgfile = 'images/model.png'
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)
    cv2.imshow('model',img)

    k=cv2.waitKey(0) & 0xFF

    if k==27:
        cv2.destroyAllWindows()
    elif k==ord('c'):
        cv2.imwrite('images/model_copy.jpg',img)
        cv2.destroyAllWindows()
        
showlmage()

