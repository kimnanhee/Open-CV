# 대칭
import cv2

image = cv2.imread("IMAGE/nanhee.jpg", cv2.IMREAD_COLOR)
image_flip_1 = cv2.flip(image, 0) # 상하 대칭
image_flip_2 = cv2.flip(image, 1) # 좌우 대칭

cv2.imshow("image", image)
cv2.imshow("image_flip_1", image_flip_1)
cv2.imshow("image_flip_2", image_flip_2)

cv2.waitKey(0)
cv2.destroyAllWindows()