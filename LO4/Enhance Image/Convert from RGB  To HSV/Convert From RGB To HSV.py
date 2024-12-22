import cv2
BGR_image = cv2.imread('download.jpeg')
cv2.imshow('image',BGR_image)
RGB_image = cv2.cvtColor(BGR_image, cv2.COLOR_BGR2RGB)
cv2.imshow('BGR_image', BGR_image)
HSV_image = cv2.cvtColor(RGB_image, cv2.COLOR_RGB2HSV)
cv2.imshow('HSV_image', HSV_image)
cv2.waitKey(0)
