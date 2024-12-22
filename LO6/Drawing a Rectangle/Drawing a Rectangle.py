import cv2
import numpy as np
image = np.ones((500, 500, 3), np.uint8)*255
x_points =(500, 400)
y_points =(400, 500)
thickness = 2
color = (0, 255, 0)
drawing_image = cv2.rectangle(image , x_points , y_points , color, thickness)
cv2.imshow('Drawing Rectangle ', drawing_image)
cv2.waitKey(0)