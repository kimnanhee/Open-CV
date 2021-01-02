# YCrCb로 피부색 검출하기
import numpy as np
import cv2

image = cv2.imread("IMAGE/hand.jpg", cv2.IMREAD_COLOR)
image = cv2.resize(image, dsize=(0, 0), fx=0.2, fy=0.2) # 0.6배 비율 조절

image_YCrCb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

mask_hand = cv2.inRange(image_YCrCb, np.array([0, 133, 77]), np.array([255, 173, 127]))
mask_color = cv2.bitwise_and(image, image, mask = mask_hand)
# mask 씌워서 피부색 검출

cv2.imshow("image", image)
# cv2.imshow("image_YCrCb", image_YCrCb)
cv2.imshow("hans", mask_color)

image_gray = cv2.cvtColor(mask_color, cv2.COLOR_BGR2GRAY) # 그레이스케일 변환
ret, binary = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY) # 이진화
binary = cv2.bitwise_not(binary)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
# cv2.findContours(이진화 이미지, 검새 방법, 근사화 방법)

for i in range(len(contours)):
    cv2.drawContours(image, [contours[i]], 0, (0, 0, 255), 2)
    # print(i, hierarchy[0][i])

cv2.imshow("contour_image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()