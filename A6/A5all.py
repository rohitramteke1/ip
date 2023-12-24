import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the input image
img = cv2.imread('view.jpg')

# Get image dimensions
rows, cols, ch = img.shape

# Define the points for affine transformation
pt1_affine = np.float32([[40, 40], [200, 40], [40, 200]])
pt2_affine = np.float32([[10, 100], [200, 50], [100, 250]])

# Define the points for perspective transformation
pt1_perspective = np.float32([[50, 65], [370, 52], [30, 387], [390, 390]])
pt2_perspective = np.float32([[0, 0], [310, 0], [0, 310], [310, 310]])

# Create a rotated image
matrix_rotated = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 0.6)
rotated_img = cv2.warpAffine(img, matrix_rotated, (cols, rows))

# Create a scaled image
scaled_img = cv2.resize(img, (cols, rows))

# Create a translated image
matrix_trans = np.float32([[1, 0, -100], [0, 1, -30]])
translated_img = cv2.warpAffine(img, matrix_trans, (cols, rows))

# Perform affine transformation
matrix_affine = cv2.getAffineTransform(pt1_affine, pt2_affine)
affine_transformed_img = cv2.warpAffine(img, matrix_affine, (cols, rows))

# Perform perspective transformation
matrix_perspective = cv2.getPerspectiveTransform(pt1_perspective, pt2_perspective)
perspective_transformed_img = cv2.warpPerspective(img, matrix_perspective, (cols, rows))

# Create a single image to display all the transformations
combined_img = np.zeros((rows, 5 * cols, ch), dtype=np.uint8)

# Copy the original image to the combined image
combined_img[:, :cols] = img

# Copy the transformed images to the combined image
combined_img[:, cols:2*cols] = affine_transformed_img
combined_img[:, 2*cols:3*cols] = perspective_transformed_img
combined_img[:, 3*cols:4*cols] = rotated_img
combined_img[:, 4*cols:] = scaled_img

# Display the combined image
plt.imshow(cv2.cvtColor(combined_img, cv2.COLOR_BGR2RGB))
plt.title('Transformations')
plt.axis('off')

# Save the combined image
output_image_path = "ALLTransformedImage.jpg"
plt.savefig(output_image_path)
plt.show()
