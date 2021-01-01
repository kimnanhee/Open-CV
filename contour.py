# 윤곽선 검출
import cv2

image = cv2.imread("IMAGE/stair.jpg", cv2.IMREAD_COLOR)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 그레이스케일 변환
ret, binary = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY) # 이진화
binary = cv2.bitwise_not(binary)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
# cv2.findContours(이진화 이미지, 검새 방법, 근사화 방법)

print(len(contours)) # 인식된 윤곽선 개수

for i in range(len(contours)):
    cv2.drawContours(image, [contours[i]], 0, (0, 0, 255), 2)
    cv2.putText(image, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
    print(i, hierarchy[0][i])
    cv2.imshow("image", image)
    cv2.waitKey(0)

cv2.destroyAllWindows()