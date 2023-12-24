import cv2
import numpy as np

img = cv2.imread(r'A4\A4.png', 0)
m, n = img.shape
mask = np.ones([3, 3], dtype=int) / 9
img_new = np.zeros([m, n], dtype=np.uint8)

for i in range(1, m-1):
    for j in range(1, n-1):
        temp = (img[i-1:i+2, j-1:j+2] * mask).sum()
        img_new[i, j] = temp.astype(np.uint8)

cv2.imwrite('blurred.png', img_new)
cv2.imshow('Original Image', img)
cv2.imshow('Blurred Image', img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()
