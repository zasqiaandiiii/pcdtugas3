import cv2
import numpy as np

img = cv2.imread('foto3.jpg')
img = cv2.resize(img, (300, 400 ))

kernel_size = (5, 5)

kernel = np.ones(kernel_size, np.float32) / (kernel_size[0] * kernel_size[1])

output = cv2.filter2D(img, -2, kernel)

cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image', output)

cv2.waitKey(0)
cv2.destroyAllWindows()
