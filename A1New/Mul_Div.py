import cv2
import numpy as np
img1 = cv2.imread('img3.png')
img2 = cv2.imread('img4.png')

def image_multiply(img1, img2, output_path):
    # Read images
    image1 = cv2.imread(img1)
    image2 = cv2.imread(img2)

    # Perform element-wise multiplication
    result_image = cv2.multiply(image1, image2)

    # Save the result image
    cv2.imwrite(output_path, result_image)

def image_divide(img1, img2, output_path):
    # Read images
    image1 = cv2.imread(img1)
    image2 = cv2.imread(img2)

    # Perform element-wise division, handling division by zero
    result_image = np.divide(image1, np.maximum(image2, 1e-10))

    # Convert the result array to uint8
    result_image = result_image.astype('uint8')

    # Save the result image
    cv2.imwrite(output_path, result_image)

# Example usage
image_multiply("image1.jpg", "image2.jpg", "output_multiply.jpg")
image_divide("image1.jpg", "image2.jpg", "output_divide.jpg")
