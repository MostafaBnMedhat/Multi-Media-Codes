from  skimage.feature import local_binary_pattern
import numpy as np
import matplotlib.pyplot as plt
import cv2

image =cv2.imread('download.jpeg',cv2.IMREAD_GRAYSCALE)
radius = 1
n_point = 8*radius
lbp_image = local_binary_pattern(image,n_point,radius, method='uniform')

lbp_hist,_ = np.histogram(lbp_image.ravel(),bins=np.arange(n_point+3),range=(0,n_point+2))
lbp_hist = lbp_hist.astype(float)/lbp_hist.sum()

plt.figure(figsize=(5,5))
plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(image,cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title('LBP Image')
plt.imshow(lbp_image,cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()

plt.figure(figsize=(5,5))
plt.title('Local Binary Pattern Histogram')
plt.bar(range(len(lbp_hist)),lbp_hist, align='center')
plt.xlabel('Levels')
plt.ylabel('Pixels')
plt.show()
