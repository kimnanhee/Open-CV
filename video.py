import cv2

# capture = cv2.VideoCapture("IMAGE/motor.mp4") # 상대 경로
capture = cv2.VideoCapture("C:/Users/DSM/Desktop/CV/practice/IMAGE/motor.mp4") # 절대 경로

while True:
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("IMAGE/motor.mp4")
    
    ret, frame = capture.read()
    frame = cv2.resize(frame, dsize=(0, 0), fx=0.5, fy=0.5) # 이미지 비율
    cv2.imshow("VideoFrame", frame)

    if cv2.waitKey(33) > 0: break

capture.release()
cv2.destroyAllWindows()