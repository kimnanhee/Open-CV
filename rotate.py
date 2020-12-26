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