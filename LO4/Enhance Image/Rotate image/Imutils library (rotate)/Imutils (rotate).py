import imutils as mu
import cv2
image = cv2.imread('../Cv2 library (rotate)/download.jpeg')
cv2.imshow('Original', image)
rotated_image = mu.rotate(image, 90)
cv2.imshow('Rotated', rotated_image)
cv2.waitKey(0)


