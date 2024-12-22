import cv2
import numpy as np
image = np.ones((500, 500, 3), np.uint8)*255
x_points =(50, 40)
y_points =(100, 100)
thickness = 2
color = (0, 255, 0)
drawing_image = cv2.line(image , x_points , y_points , color, thickness)
cv2.imshow('Drawing Straight Line', drawing_image)
cv2.waitKey(0)