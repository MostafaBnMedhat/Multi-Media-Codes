import cv2
image = cv2.imread('Median_image.png')
cv2.imshow('Original', image)
median_filter = cv2.medianBlur(image, 9)
# ksize is a kernel size and should be odd number
cv2.imshow('Median Filter', median_filter)
cv2.waitKey(0)