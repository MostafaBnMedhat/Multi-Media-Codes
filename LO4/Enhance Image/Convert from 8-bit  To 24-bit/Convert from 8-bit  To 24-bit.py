import cv2
image = cv2.imread('download.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Original', image)
colorImage = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
colorImage[:,:,0]= 0
colorImage[:,:,1]= 0
cv2.imshow('colorImage', colorImage)
cv2.waitKey(0)
