import cv2
import numpy as np
import matplotlib.pyplot as plt

binary = cv2.imread('binary_image.jpg', 0)
_, binary = cv2.threshold(binary, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((5,5), np.uint8)

dilated = cv2.dilate(binary, kernel, iterations=1)
eroded = cv2.erode(binary, kernel, iterations=1)

opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

titles = ['Original', 'Dilation', 'Erosion', 'Opening', 'Closing']
images = [binary, dilated, eroded, opening, closing]

for i in range(5):
 plt.subplot(1,5,i+1)
 plt.imshow(images[i], cmap='gray')
 plt.title(titles[i])
 plt.axis('off')

plt.show()
