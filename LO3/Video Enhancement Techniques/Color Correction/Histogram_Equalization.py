import cv2

video = cv2.VideoCapture('input3_video.mp4')
while True :
    ret, frame = video.read()
    if not  ret:
        break
    YUV_Color = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    YUV_Color[:, :, 0] = cv2.equalizeHist(YUV_Color[:, :, 0])
    EnhancementVideo = cv2.cvtColor(YUV_Color, cv2.COLOR_YUV2BGR)
    cv2.imshow('EqualizeHist Filter',EnhancementVideo)
    if cv2.waitKey(1) == ord('q') :
        break
video.release()
cv2.destroyAllWindows()

