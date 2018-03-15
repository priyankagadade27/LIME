import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import ImageEnhance

img = cv2.imread('img/inp_10.jpg', 1)
cv2.imshow("Original image",img)

#image enhancer
# enhancer = ImageEnhance.Sharpness('img/inp_16.jpg')

# for i in range(8):
#     factor = i / 4.0
#     enhancer.enhance(factor).show("Sharpness %f" % factor)

# CLAHE (Contrast Limited Adaptive Histogram Equalization)
clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
l, a, b = cv2.split(lab)  # split on 3 different channels

l2 = clahe.apply(l)  # apply CLAHE to the L-channel

lab = cv2.merge((l2,a,b))  # merge channels
img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BGR
cv2.imshow('Output ', img2)
#cv2.imwrite('sunset_modified.jpg', img2)

# Smoothning Image

blur = cv2.GaussianBlur(img,(5,5),0)


plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

cv2.imshow('Output ', img2)