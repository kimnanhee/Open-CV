# YCrCb로 손 이미지를 검출해서, 손가락 개수 인식하기
import numpy as np
import cv2

image = cv2.imread("IMAGE/hand.jpg", cv2.IMREAD_COLOR)
image = cv2.resize(image, dsize=(0, 0), fx=0.15, fy=0.15) # 0.15배 비율 조절
image_blur = cv2.blur(image, (9, 9), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT) # 흐림 처리
image_YCrCb = cv2.cvtColor(image_blur, cv2.COLOR_BGR2YCrCb)

mask_hand = cv2.inRange(image_YCrCb, np.array([0, 133, 77]), np.array([255, 173, 127])) # 피부색 범위
mask_color = cv2.bitwise_and(image_blur, image_blur, mask = mask_hand)
# mask 씌워서 피부색 검출

cv2.imshow("image", image)
cv2.imshow("blur", image_blur)
# cv2.imshow("image_YCrCb", image_YCrCb)
cv2.imshow("hans", mask_color)

image_gray = cv2.cvtColor(mask_color, cv2.COLOR_BGR2GRAY) # 그레이스케일 변환
ret, binary = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY) # 이미지 이진화
binary = cv2.bitwise_not(binary)

transform = cv2.distanceTransform(cv2.bitwise_not(binary), cv2.DIST_L2, 5)
result = cv2.normalize(transform, None, 255, 0, cv2.NORM_MINMAX, cv2.CV_8UC1)
cv2.minMaxIdx()

cv2.imshow("transform", result)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
# 테두리 검출 cv2.findContours(이진화 이미지, 검새 방법, 근사화 방법)

for i in range(len(contours)):
    cv2.drawContours(image, [contours[i]], 0, (0, 0, 255), 2)
    # print(i, hierarchy[0][i])

cv2.imshow("contour_image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()