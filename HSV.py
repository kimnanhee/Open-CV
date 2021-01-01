# HSV(Hue Saturation Value) 색상 검출
import cv2

image = cv2.imread("IMAGE/rainbow_tomato.jpg", cv2.IMREAD_COLOR)
image = cv2.resize(image, dsize=(0, 0), fx=0.6, fy=0.6) # 0.6배 비율 조절

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # HSV채널로 변경
h, s, v = cv2.split(hsv) # 각각의 속성으로 분할


cv2.imshow("image", image)
# cv2.imshow("hsv", hsv)
# cv2.imshow("h", h)
# cv2.imshow("s", s)
# cv2.imshow("v", v)

cv2.waitKey(0)
cv2.destroyAllWindows()