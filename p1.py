import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)

f = img.astype(np.float64)
c = 255 / np.log(1 + np.max(f))
log_transformed = np.array(c * np.log(1 + f), dtype=np.uint8)

gamma = 0.5
gamma_corrected = np.array(255 * (img / 255) ** gamma, dtype=np.uint8)

alpha = 1.5
beta = 50
contrast_adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

titles = ['Original', 'Log Transform', 'Gamma Correction', 'Contrast Adjusted']
images = [img, log_transformed, gamma_corrected, contrast_adjusted]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()
