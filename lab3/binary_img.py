import numpy as np
import math
import cv2
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

matplotlib.use('agg')


img = cv2.imread("pointbased/100zloty.jpg", 0)

x, y = img.shape[:2]

array_of_binary = []

for i in range(8):
    array_of_binary.append(np.zeros([x, y], dtype=np.uint8))



for i in range(0, x):
    for j in range(0, y):
        bits = img[i, j]
        counter = 128
        sum = 0
        for k in range(8):
            result = bits & counter
            if result == counter:
                sum += result
            array_of_binary[k][i, j] = result
            counter = counter >> 1


gs = gridspec.GridSpec(3, 4)
plt.figure(1)



plt.subplot(gs[0, :])
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.title('Original')

for i in range(8):
    if i < 4:
        plt.subplot(gs[1, i])
        plt.imshow(array_of_binary[i], cmap='gray')
        plt.axis('off')
        plt.title(str(i+1) + 'st')
    else:
        plt.subplot(gs[2, (i - 4)])
        plt.imshow(array_of_binary[i], cmap='gray')
        plt.axis('off')
        plt.title(str(i+1) + 'st')

plt.show()

# cv2.imshow('Original_grey', img)
# cv2.waitKey(0)