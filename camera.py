# 카메라 출력
import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 600) # 비디오 프레임 가로 크기
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 400) # 비디오 프레임 세로 크기

while True:
    ret, frame = capture.read() # 프레임 캡쳐
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) > 0: break

capture.release()
cv2.destroyAllWindows()