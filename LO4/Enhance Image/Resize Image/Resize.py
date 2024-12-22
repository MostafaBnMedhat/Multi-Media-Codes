import cv2
image = cv2.imread('download.jpeg')
rows, cols = image.shape[:2]
rows = int(rows*3)
cols = int(cols*3)
resized = cv2.resize(image, (rows, cols))
cv2.imshow('Original image', image)
cv2.imshow('Resized image', resized)
cv2.waitKey(0)