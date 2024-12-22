import cv2
import numpy as np
image = np.ones((500, 500, 3), np.uint8)*255
center = (250, 250)
y_points = 100
color = (0, 255, 0)

drawing_image =cv2.circle(image, center, y_points, color, -1)
cv2.imshow('Drawing Straight Line', drawing_image)
cv2.waitKey(0)