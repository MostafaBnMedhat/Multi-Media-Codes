import cv2
image = cv2.imread('download.jpeg')
alpha = 4
beta = 10
cv2.imshow('Original', image)
newImage = cv2.convertScaleAbs(image, alpha=alpha , beta=beta)
cv2.imshow('Blending', newImage)
cv2.waitKey(0)