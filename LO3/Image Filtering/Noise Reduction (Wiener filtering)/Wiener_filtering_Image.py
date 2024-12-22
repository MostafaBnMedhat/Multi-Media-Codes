import cv2
import numpy as np
from scipy.signal import wiener

image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Original', image)
winner_filter = wiener(image)
print(winner_filter)
winner_filter = np.clip(winner_filter, 0, 255).astype('uint8')
print(winner_filter)
cv2.imshow('Filtered', winner_filter)
cv2.waitKey(0)

