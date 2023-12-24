
#Scaling Transformation 
import cv2
import numpy as np

img = cv2.imread('view.jpg')

scaled_img = cv2.resize(img, None, fx=0.6, fy=0.6)

cv2.imshow("Scaled image",scaled_img)
cv2.imwrite("ScaledImage.png",scaled_img)
cv2.waitKey(0)
cv2.destroyAllWindows()