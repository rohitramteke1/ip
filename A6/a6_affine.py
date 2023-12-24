# Affine Transformation
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('view.jpg')
rows,cols,ch = img.shape

pt1 = np.float32([[40,40],[200,40],[40,200]])
pt2 = np.float32([[10,100],[200,50],[100,250]])

matrix_aff = cv2.getAffineTransform(pt1,pt2)
dst = cv2.warpAffine(img,matrix_aff,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')

output_image_path = "Affine.jpg"
plt.savefig(output_image_path)
plt.show()
