import cv2
import numpy as np
def Encoding(data):
    counter = 1
    prev_element = data[0]
    encodedData = []
    for element in data:
        if element == prev_element:
            counter += 1
        else:
            encodedData.extend([counter,prev_element])
            prev_element = element
            counter = 1
    encodedData.extend([counter,prev_element])
    return encodedData

image = cv2.imread('download.jpeg')
GrayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
FlattenedImage = GrayImage.flatten()
ImageCompression = Encoding(FlattenedImage)
np.save('FlattenedImage.npy', ImageCompression)
cv2.imshow('The Gray image', GrayImage)
cv2.waitKey(0)

