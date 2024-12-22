import cv2

video = cv2.VideoCapture('input4_video.mp4')
brightness = 30
contrast = 10
while True :
    ret, frame = video.read()
    if not  ret:
     break

    EnhancementVideo = cv2.convertScaleAbs(frame,alpha=1+ contrast /127.0 ,beta= brightness )
    cv2.imshow('EqualizeHist Filter',EnhancementVideo)
    if cv2.waitKey(1) == ord('q') :
        break
video.release()
cv2.destroyAllWindows()

