# Opcn-CV 시작하기

{:toc}

## 설치하기

```python
python -m pip install opencv-python

버전확인
import cv2
print(cv2.__version__)
```



## 카메라 출력(Camera)

```python
import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

while True:
    ret, frame = capture.read()
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) > 0: break

capture.release()
cv2.destroyAllWindows()
```

설정

​	`capture = cv2.ViedeoCapture(0)` 카메라에서 영상을 받아오기

​	`capture.set(option, n)` 카메라 속성 설정하기



출력

​	while문으로 영상 출력 반복하기

​	`ret, frame = capture.read()` frame에 현재 프레임이 저장된다

​	`cv2.imshow('창 제목', 이미지)` 윈도우 창에 이미지를 띄운다



종료

​	`caption.release()` 카메라에서 받아온 메모리 해제

​	`cv2.destroyAllWindows()` 모든 윈도우 창 닫기



## 이미지 출력(Image)

```python
import cv2

image = cv2.imread("IMAGE/nanhee.jpg", cv2.IMREAD_ANYCOLOR) # 원본
# image = cv2.imread("IMAGE/nanhee.jpg", cv2.IMREAD_GRAYSCALE) # 그레이
# image = cv2.imread("IMAGE/nanhee.jpg", cv2.IMREAD_COLOR) # BGR

height, width, channel = image.shape

cv2.imshow("nanhee", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

설정

​	`image = cv2.imread("IMAGE/nanhee.jpg", cv2.IMREAD_ANYCOLOR)` IMAGE폴더 밑에 `nanhee.jpg` 파일을 원본으로 가져오기



## 동영상 출력(Video)

```python
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
```

설정

​	`capture = cv2.VideoCapture("경로")` 동영상 파일에서 프레임을 받아온다.
​	상대 경로로 테스트 해보니 오류 발생, 절대 경로의 동영상 파일을 받아왔다.



출력

​	`capture.get(속성)` 으로 capture의 속성을 사용할 수 있다.

​	`cv2.CAP_PROP_POS_FRAMES` 현재 프레임의 개수

​	`cv2.CAP_PROP+FRAME_COUNT` 총 프레임의 개수

​	`현재 프레임의 개수 == 총 프레임의 개수` 일 경우, 마지막 프레임이므로 동영상 파일을 다시 불러온다.

`  frame = cv2.resize(frame, dsize=(0, 0), fx=0.5, fy=0.5)` 동영상 파일의 비율을 조절할 수 있다.

​	`cv2.waitKey(time)` time마다 프레임을 재생한다.