import cv2

video = cv2.VideoCapture('input1_video.mp4')
kernel_size = (1,3)

while True :
    ret, frame = video.read()
    if not  ret:
        break
    EnhancementVideo = cv2.GaussianBlur(frame,kernel_size,0)
    cv2.imshow('Gaussian Filter',EnhancementVideo)
    if cv2.waitKey(1) == ord('q') :
        break
video.release()
cv2.destroyAllWindows()

