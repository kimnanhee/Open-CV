# 자르기
import cv2

image = cv2.imread("IMAGE/nanhee.jpg", cv2.IMREAD_COLOR)

image_slice = image.copy()
image_slice = image[150:550, 200:550] # 높이, 너비

cv2.imshow("image", image)
cv2.imshow("image_slice", image_slice)

cv2.waitKey(0)
cv2.destroyAllWindows()