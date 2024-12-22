import cv2
image = cv2.imread('download.jpeg', cv2.IMREAD_GRAYSCALE)
# OR
#image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('image', image)
cv2.waitKey(0)
