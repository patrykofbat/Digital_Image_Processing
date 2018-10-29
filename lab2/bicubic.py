import numpy as np
import math
import cv2
import scipy.io
import time


def getX(I, i, j):
    return ((I[i+1, j][0]) - (I[i-1, j][0]))/2

def getY(I, i, j):
    return ((I[i, j+1][0]) - (I[i, j-1][0]))/2

def getXY(I, i, j):
    return ((I[i+1, j+1][0]) - (I[i-1, j][0]) - (I[i, j-1][0]) - (I[i, j][0]))/4

def getXVector(I, i, j, func):
    x = []
    x.append(func(I, i, j)) #a
    x.append(func(I, i + 1, j)) #b
    x.append(func(I, i, j + 1)) #d
    x.append(func(I, i + 1, j + 1)) #c
    return x


img = np.double(cv2.imread("archiwum/parrot.bmp"))

xReScale = 3
yReScale = 5

x, y = img.shape[:2]

newY, newX = math.floor(xReScale * x), math.floor(yReScale * y)


newParrot = np.zeros([newX, newY, 3], dtype=np.double)


xStep = x/newX
yStep = y/newY

A_input = scipy.io.loadmat("archiwum/a1.mat")['A1']

A = np.matrix(A_input)

start_time = time.time()
for i in range(0, newX):
    for j in range(0, newY):
        xVector = []
        ii = i * xStep
        jj = j * yStep
        i1 = math.floor(ii)
        j1 = math.floor(jj)

        if i1 + 2 > x - 1:
            i1 = x - 3

        if j1 + 2 > y - 1:
            j1 = y - 3

        a = img[i1, j1][0]
        b = img[i1 + 1, j1][0]
        c = img[i1 + 1, j1 + 1][0]
        d = img[i1, j1 + 1][0]

        xVector.append(a)
        xVector.append(b)
        xVector.append(d)
        xVector.append(c)

        xVector += getXVector(img, i1, j1, getX)
        xVector += getXVector(img, i1, j1, getY)
        xVector += getXVector(img, i1, j1, getXY)

        xVector = np.matrix(xVector)

        a = A * xVector.transpose()

        sum = 0

        iN = ii % 1
        jN = jj % 1



        for k in range(0, 4):
            for p in range(0, 4):
                sum += a.transpose()[0, k + (p * 4)] * (iN ** k) * (jN ** p)

        newParrot[i, j] = sum

print("--- %s seconds ---" % (time.time() - start_time))

resized = cv2.resize(np.uint8(img), (0, 0), fx=xReScale,fy=yReScale, interpolation = cv2.INTER_CUBIC)
cv2.imshow('old image bicubic', np.uint8(img))
cv2.imshow('new image bicubic', np.uint8(newParrot))
cv2.imshow('old image bicubic', np.uint8(resized))

cv2.waitKey(0)

## nearest_neighbor --- 0.21530508995056152 seconds ---
## bilinear --- 4.099877595901489 seconds ---
## bicubic --- 12.058842182159424 seconds ---