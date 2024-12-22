import cv2
from skimage.restoration import denoise_tv_chambolle
image = cv2.imread('download.jpeg')
cv2.imshow('Original', image)
skimage_image = denoise_tv_chambolle(image)
cv2.imshow('skimage', skimage_image)
cv2.waitKey(0)