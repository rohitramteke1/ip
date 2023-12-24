import cv2
import numpy as np
	
image1 = cv2.imread('img1.jpg')
image2 = cv2.imread('img2.jpg')

#Arithmatic Operation 
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
cv2.imshow('Weighted Image', weightedSum)

sub = cv2.subtract(image1, image2)
cv2.imshow('Subtracted Image', sub)


#Logical Operation 
img1 = cv2.imread('img3.png')
img2 = cv2.imread('img4.png')

#Bitwise AND Operation 
dest_and = cv2.bitwise_and(img2, img1, mask = None)

# with the Bitwise AND operation
# on the input images
cv2.imshow('Bitwise And', dest_and)


#Bitwise OR Operation
dest_or = cv2.bitwise_or(img2, img1, mask = None)

# with the Bitwise OR operation
# on the input images
cv2.imshow('Bitwise OR', dest_or)


#Bitwise NOT Operation 
dest_not1 = cv2.bitwise_not(img1, mask = None)
dest_not2 = cv2.bitwise_not(img2, mask = None)

# with the Bitwise NOT operation
# on the 1st and 2nd input image
cv2.imshow('Bitwise NOT on image 1', dest_not1)
cv2.imshow('Bitwise NOT on image 2', dest_not2)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27: # Press "ESC" used to close all windows
	cv2.destroyAllWindows()
