import cv2
import numpy as np
from matplotlib import pyplot as plt

def apply_fourier_transform(image_path):
    # Read the input image in color
    original_image_color = cv2.imread(image_path)

    if original_image_color is None:
        print('Error: Could not open or find the image.')
        return

    # Convert the color image to grayscale
    original_image_gray = cv2.cvtColor(original_image_color, cv2.COLOR_BGR2GRAY)

    # Apply Fourier Transform
    fourier_transform = np.fft.fft2(original_image_gray)
    # Shift the zero frequency component to the center
    fourier_transform_shifted = np.fft.fftshift(fourier_transform)
    # Compute the magnitude spectrum
    magnitude_spectrum = 20 * np.log(np.abs(fourier_transform_shifted))

    # Display the original color image, its grayscale version, and Fourier Transform magnitude spectrum
    plt.figure(figsize=(15, 5))

    plt.subplot(131)
    plt.imshow(cv2.cvtColor(original_image_color, cv2.COLOR_BGR2RGB))
    plt.title('Original Color Image')

    plt.subplot(132)
    plt.imshow(original_image_gray, cmap='gray')
    plt.title('Grayscale Image')

    plt.subplot(133)
    plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Fourier Transform Magnitude Spectrum')

    plt.show()

if __name__ == "__main__":
    # Replace 'input_image.jpg' with the path to your own image file
    input_image_path = 'Cheetah.jpg'

    # Apply Fourier Transform and display the results
    apply_fourier_transform(input_image_path)
