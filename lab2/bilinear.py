import numpy as np
import math
import cv2
import time

img = np.double(cv2.imread("archiwum/parrot.bmp"))

xReScale = 3
yReScale = 5

x, y = img.shape[:2]

newY, newX = math.floor(xReScale * x), math.floor(yReScale * y)

newParrot = np.zeros([newX, newY, 3], dtype=np.double)

xStep = x/newX
yStep = y/newY

start_time = time.time()
for i in range(0, newX):
    for j in range(0, newY):

        ii = i * xStep
        jj = j * yStep
        i1 = math.floor(ii)
        j1 = math.floor(jj)

        if i1 + 1 > x - 1:
            i1 = x - 2

        if j1 + 1 > y - 1:
            j1 = y - 2

        a = img[i1, j1]
        b = img[i1 + 1, j1]
        c = img[i1 + 1, j1 + 1]
        d = img[i1, j1 + 1]

        A = np.matrix([[a[0], d[0]],
                       [b[0], c[0]]])

        iN = ii % 1
        jN = jj % 1

        newParrot[i, j] = [1-iN, iN] * A * np.matrix([[1 - jN], [jN]])

print("--- %s seconds ---" % (time.time() - start_time))


cv2.imshow('old image bilinear', np.uint8(img))
cv2.imshow('new image bilinear', np.uint8(newParrot))
cv2.waitKey(0)
