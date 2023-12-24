# import cv2
# import numpy as np



# # Loop runs if capturing has been initialized.
# while True:
#     # Reads frames from a camera
#     image = cv2.imread("ABC.jpg")

#     # Converts to HSV color space; OpenCV reads colors as BGR
#     # Frame is converted to HSV
#     hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#     # Defining the range of blue color in HSV
#     blue1 = np.array([110, 50, 50])
#     blue2 = np.array([130, 255, 255])

#     # Initializing the mask to be convoluted over the input image
#     mask = cv2.inRange(hsv, blue1, blue2)

#     # Applying bitwise_and operation over each pixel convoluted
#     res = cv2.bitwise_and(image, image, mask=mask)

#     # Defining the kernel (structuring element)
#     kernel = np.ones((5, 5), np.uint8)

#     # Defining the opening function over the image and structuring element
#     opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

#     # Display the mask and opening operation in separate windows
#     cv2.imshow('Mask', mask)
#     cv2.imshow('Opening', opening)
#     cv2.imwrite('Masked.png', mask)
#     cv2.imwrite('OpeningImage.png', opening)

#     # Wait for 'q' key to stop the program
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # De-allocate any associated memory usage
# cv2.destroyAllWindows()

# # Close the window / Release the webcam
# screenRead.release()
