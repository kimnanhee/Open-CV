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