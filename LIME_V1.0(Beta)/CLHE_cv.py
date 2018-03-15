import numpy as np
import cv2

img = cv2.imread('img/inp_13.jpg',0)

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv2.imwrite('img/out_c_13.jpg',cl1)


