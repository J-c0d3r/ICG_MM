import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

imageFile = 'VluSkJ.jpg'
img = np.array(Image.open(imageFile))[:, :, :3]
(l, c ,p) = img.shape
plt.imshow(img)

# converter para escala de cinza:
imgGray = np.zeros(shape=(l, c), dtype=np.uint8)
for i in range(l):
    for j in range(c):
        r = float(img[i, j, 0])
        g = float(img[i, j, 1])
        b = float(img[i, j, 2])

        imgGray[i, j] = (r + g + b) / 3

plt.figure(figsize=(16, 16))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.subplot(1, 2, 2)
plt.imshow(imgGray, cmap='gray')

