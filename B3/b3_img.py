import cv2
import numpy as np

# Prompt the user for the image file path
# image_path = input("Enter the path to the image file: ")

try:
    # Load the user-provided image
    frame = cv2.imread('person3.jpg')

    if frame is None:
        print("Error: Could not load the image. Please check the file path.")
    else:
        # Convert to grayscale for edge detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Calculation of Sobelx
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)

        # Calculation of Sobely
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)

        # Calculation of Laplacian
        laplacian = cv2.Laplacian(gray, cv2.CV_64F)

        cv2.imshow('Original Image', frame)
        cv2.imshow('SobelX', sobelx)
        cv2.imshow('SobelY', sobely)
        cv2.imshow('Laplacian', laplacian)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

except Exception as e:
    print(f"An error occurred: {str(e)}")
