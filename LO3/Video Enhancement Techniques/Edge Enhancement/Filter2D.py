import cv2
import numpy as np
video= cv2.VideoCapture('input2_video.mp4')
kernel= np.array(
    [
        -1, -1, -1,
        -1 ,9 ,-1,
        -1 ,-1 , -1
    ]
)
while True:
    ret, frame = video.read()
    if not ret:
        break
    EnhancementVideo = cv2.filter2D(frame, -1, kernel)
    cv2.imshow('Filter2D Filter', EnhancementVideo)
    if cv2.waitKey(1) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
