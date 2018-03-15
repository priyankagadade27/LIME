from __future__ import division
import cv2
import numpy as np
from matplotlib import pyplot as plt

import fun1

#img = cv2.imread('res_27_3.jpg',0)

for i in range(2,13):
	img = cv2.imread('img/inp_4.jpg',0)
	equ = cv2.equalizeHist(img)
	res = np.hstack((img,equ)) #stacking images side-by-side
	cv2.imwrite('img/output.jpg',res)

img = cv2.imread('img/output.jpg',0)
# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)

# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()

#Smoothing Images
#blur = cv2.blur(img,(5,5))
blur = cv2.GaussianBlur(img,(5,5),0)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()


#Show Actual Output and input
#img = cv2.imread('img/output.jpg',0)
screen_res = 1280, 720
scale_width = screen_res[0] / img.shape[1]
scale_height = screen_res[1] / img.shape[0]
scale = min(scale_width, scale_height)
window_width = int(img.shape[1] * scale)
window_height = int(img.shape[0] * scale)

cv2.namedWindow('dst_rt', cv2.WINDOW_NORMAL)
cv2.resizeWindow('dst_rt', window_width, window_height)

cv2.imshow('dst_rt', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

