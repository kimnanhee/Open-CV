import cv2

image = cv2.imread("IMAGE/nanhee.jpg")

image_1 = cv2.resize(image, dsize=(500, 400)) # 픽셀 조절
image_2 = cv2.resize(image, dsize=(0, 0), fx=0.6, fy=0.6) # 비율 조절

cv2.imshow("image", image)
cv2.imshow("image_1", image_1)
cv2.imshow("image_2", image_2)

cv2.waitKey(0)
cv2.destroyAllWindows()