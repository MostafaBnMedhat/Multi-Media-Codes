import numpy as np
import cv2
image = cv2.imread('download.jpeg')
rows, cols = image.shape[:2]
t_x = 50
t_y = 100
matrix = np.float32([[1, 0, t_x], [0, 1, t_y]])
transformed_image = cv2.warpAffine(image, matrix, (cols, rows))
cv2.imshow('Original', image)
cv2.imshow('Transformed', transformed_image)
cv2.waitKey(0)
