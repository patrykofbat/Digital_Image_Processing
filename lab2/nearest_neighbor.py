import numpy as np
import math
import cv2
import time

img = cv2.imread("archiwum/parrot.bmp")

xReScale = 3
yReScale = 5

x, y = img.shape[:2]

newY, newX = math.floor(xReScale * x), math.floor(yReScale * y)

newParrot = np.zeros([newX, newY, 3], dtype=np.uint8)

xStep = x/newX
yStep = y/newY

start_time = time.time()
for i in range(0, newX):
    for j in range(0, newY):

        ii = round(i * xStep)
        jj = round(j * yStep)

        if ii > x-1:
            ii = x-1

        if jj > y-1:
            jj = y-1

        newParrot[i, j] = img[ii, jj]

print("--- %s seconds ---" % (time.time() - start_time))

cv2.imshow('old image nn', img)
cv2.imshow('new image nn', newParrot)
cv2.waitKey(0)



