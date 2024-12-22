
import cv2
image = cv2.imread('download.jpeg')
cv2.imshow('Original', image)
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated', rotated_image)
cv2.waitKey(0)


