import cv2
import numpy as np
image = np.ones((500, 600, 3), np.uint8)*255
# x_points =(300, 200)
# y_points =(100, 100)
# thickness = 2
# color = (0, 255, 0)
# line_image = cv2.line(image , x_points , y_points , color, thickness)
# rectangle_image = cv2.rectangle(line_image , x_points , y_points , color, thickness)
# cv2.imshow('Drawing Straight Line', rectangle_image)
# cv2.waitKey(0)

X_line =(50 , 50)
Y_line =(350,350)
X_rectangle = (300 , 300)
Y_rectangle = (100,100)
thickness = 2
color = (0, 255, 0)
if X_line > X_rectangle: X_line = X_rectangle
if Y_line > Y_rectangle: Y_line = Y_rectangle
if Y_line < Y_rectangle: Y_line = Y_rectangle
if X_line < X_rectangle: X_line = X_rectangle
line_image = cv2.line(image , X_line , Y_line , color, thickness)
rectangle_image = cv2.rectangle(image , X_rectangle , Y_rectangle , color, thickness)


cv2.imshow('Drawing ', rectangle_image)


cv2.waitKey(0)
