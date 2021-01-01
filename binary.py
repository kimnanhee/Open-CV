# 이진화
import cv2

image = cv2.imread("IMAGE/stair.jpg", cv2.IMREAD_COLOR)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 그레이스케일 변환
ret, dst = cv2.threshold(image_gray, 100, 255, cv2.THRESH_BINARY)
# cv2.threshold(그레이스케일 이미지, 임계값, 최댓값, 임계값 종류)
# 임계값 이하는 0, 이상이면 최댓값으로 변경

# cv2.imshow("gray", image_gray)
cv2.imshow("image", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()