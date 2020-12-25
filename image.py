import cv2

image = cv2.imread("IMAGE/nanhee.jpg", cv2.IMREAD_ANYCOLOR) # 원본
# image = cv2.imread("IMAGE/nanhee.jpg", cv2.IMREAD_GRAYSCALE) # 그레이
# image = cv2.imread("IMAGE/nanhee.jpg", cv2.IMREAD_COLOR) # BGR

height, width, channel = image.shape
print(height, width, channel) # 이미지 정보 출력
# channel이 3이면 다색 이미지, 1이면 단색 이미지

cv2.imshow("nanhee", image)
cv2.waitKey(0)
cv2.destroyAllWindows()