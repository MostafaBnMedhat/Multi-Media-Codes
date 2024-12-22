import cv2
import imutils as mu
import numpy as np
image = np.ones((500, 500, 3), np.uint8)*255
x_points =(200, 200)
y_points =(400, 300)
thickness = 2
color = (0, 255, 0)
drawing_image = cv2.rectangle(image , x_points , y_points , color, thickness)
cv2.imshow('Drawing Rectangle ', drawing_image)
rotated_image = mu.rotate(image,90)
# Or can use cv2.rotate
cv2.imshow('Rotated Rectangle ', rotated_image)
cv2.waitKey(0)