import cv2
import numpy as np

# Capture livestream video content from camera 0
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    while True:
        # Take each frame
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert to HSV for simpler calculations
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Calculation of Sobelx
        sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
        
        # Calculation of Sobely
        sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
        
        # Calculation of Laplacian
        laplacian = cv2.Laplacian(frame, cv2.CV_64F)
        
        cv2.imshow('sobelx', sobelx)
        cv2.imshow('sobely', sobely)
        cv2.imshow('laplacian', laplacian)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()

    # Release the frame
    cap.release()
