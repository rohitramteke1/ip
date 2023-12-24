#Scaling Transformation

import cv2
import numpy as np

img = cv2.imread('view.jpg')
rows, cols, ch = img.shape

matrix_trans = np.float32([[1, 0, -100], [0, 1, -30]])
translated_img = cv2.warpAffine(img, matrix_trans, (cols, rows))

cv2.imshow("Translated image", translated_img)
cv2.imwrite("Translatedimage.png", translated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
