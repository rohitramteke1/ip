
#Persceptive Transformation
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('view.jpg')
rows,cols,ch = img.shape

pt1 = np.float32([[50,65],[370,52],[30,387],[390,390]])
pt2 = np.float32([[0,0],[310,0],[0,310],[310,310]])

matrix_aff = cv2.getPerspectiveTransform(pt1,pt2)
dst = cv2.warpPerspective(img,matrix_aff,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')

output_image_path = "PersecptiveTransform.jpg"
plt.savefig(output_image_path)
plt.show()