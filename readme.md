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



## 대칭 

``` python
import cv2

image = cv2.imread("IMAGE/nanhee.jpg", cv2.IMREAD_COLOR)
image_flip_1 = cv2.flip(image, 0) # 상하
image_flip_2 = cv2.flip(image, 1) # 좌우

cv2.imshow("image", image)
cv2.imshow("image_flip_1", image_flip_1)
cv2.imshow("image_flip_2", image_flip_2)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

설정

​	`cv2.flip(이미지, 대칭 방법)` 이미지를 방법에 따라서 대칭으로 만들 수 있다.

​	대칭 방법이 `0` 이면 상하, `1` 이면 좌우 방향으로 대칭



## 회전

```python
import cv2

image = cv2.imread("IMAGE/nanhee.jpg")

height, width, channel = image.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1) # 회전 배열
# (중심점 x좌표, 중심점 y좌표), 회전할 각도, 확대 비율
image_rotate = cv2.warpAffine(image, matrix, (width, height))

cv2.imshow("image", image)
cv2.imshow("image_rotate", image_rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

설정

​	`matrix` 에 `회전 배열` 을 저장한다.

​	`cv2.getRotationMatrix2D((중심점 x좌표, 중심점 y좌표), 회전할 각도, 확대 비율)` 

​	`cv2.warpAffine(이미지, 회전 배열, (이미지 너비, 이미지 높이))` 결과 이미지를 배열에 따라 회전시키고, 너비와 높이를 설정한다.



## 가장자리 검출

```python
import cv2

image = cv2.imread("IMAGE/nanhee.jpg", cv2.IMREAD_COLOR)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(image, 100, 255)
sobel = cv2.Sobel(image_gray, cv2.CV_8U, 1, 0, 3)
laplacian = cv2.Laplacian(image_gray, cv2.CV_8U, ksize=3)

cv2.imshow("image", image)
cv2.imshow("canny", canny)
cv2.imshow("sobel", sobel)
cv2.imshow("laplacian", laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

설정

​	Canny - `cv2.Canny(이미지, 임계값1, 임계값2, 커널 크기, L2그라디언트)`

​	Sobel - `cv2.Sobel(그레이스케일 이미지, 정밀도, x방향 미분, y방향 미분, 커널, 배율 델타, 픽셀, 외삼법)`

​	Laplacian - `cv2.Laplacian(그레이스케일 이미지, 정밀도 커널, 배율, 델타, 픽셀 외삼법)`



## 코너 검출

```python
import cv2

image_color = cv2.imread("IMAGE/stair.jpg", cv2.IMREAD_COLOR)

image_gray = cv2.cvtColor(image_color, cv2.COLOR_RGB2GRAY) # 회색조로 변경
corners = cv2.goodFeaturesToTrack(image_gray, 100, 0.01, 5, blockSize=3, useHarrisDetector=True, k=0.03) # 코너 검출

for i in corners:
    cv2.circle(image_color, tuple(i[0]), 3, (0, 0, 255), 2) # 원으로 지점 표시

cv2.imshow("image", image_color)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

설정

​	`cv2.goodFeaturesToTrack()`으로 윤곽선들의 이미지에서 코너를 검출한다.

​	`cv2.goodFeaturesToTrack(이미지, 코너 최댓값, 코너 품질, 회소 거리, 마스크, 블록 크기, 해리스 코너 검출기 유/무, 해리스 코너 개수)`

​	코너 검출을 통해서 `corners`가 반환되고, 배열안에 코너들의 좌표가 들어있다.

​	`cv2.circle(이미지, 중심 과표, 반지름, BGR, 두께)`로 이미지에 원으로 코너를 그려준다.