# 직선 검출 - 점진성 확률적 하프 변환
import numpy as np
import cv2

image = cv2.imread("IMAGE/stair.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(image_gray, 5000, 1500, apertureSize = 5, L2gradient = True)
lines = cv2.HoughLinesP(canny, 0.8, np.pi / 180, 90, minLineLength = 10, maxLineGap = 100)

for i in lines:
    cv2.line(image, (i[0][0], i[0][1]), (i[0][2], i[0][3]), (0, 0, 255), 2)

cv2.imshow("image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()