# 가장자리 검출
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