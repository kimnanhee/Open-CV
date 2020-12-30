# 그레이스케일 설정
import cv2

image = cv2.imread("IMAGE/nanhee.jpg", cv2.IMREAD_COLOR)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("image", image)
cv2.imshow("image_gray", image_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()