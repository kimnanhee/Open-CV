# 코너 검출
import cv2

image_color = cv2.imread("IMAGE/stair.jpg", cv2.IMREAD_COLOR)

image_gray = cv2.cvtColor(image_color, cv2.COLOR_RGB2GRAY) # 회색조로 변경
corners = cv2.goodFeaturesToTrack(image_gray, 100, 0.01, 5, blockSize=3, useHarrisDetector=True, k=0.03) # 코너 검출

for i in corners:
    cv2.circle(image_color, tuple(i[0]), 3, (0, 0, 255), 2) # 원으로 지점 표시

cv2.imshow("image", image_color)

cv2.waitKey(0)
cv2.destroyAllWindows()