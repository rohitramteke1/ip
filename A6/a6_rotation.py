#Rotation Transformation

import cv2
import numpy as np

img = cv2.imread('view.jpg')
rows, cols, ch = img.shape

matrix_rotated = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 0.6)
rotated_img = cv2.warpAffine(img, matrix_rotated, (cols, rows))

cv2.imshow("Rotated image",rotated_img)
cv2.imwrite("RotatedImage.png",rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()