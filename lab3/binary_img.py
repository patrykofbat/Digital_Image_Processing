import numpy as np
import math
import cv2

img = cv2.imread("pointbased/100zloty.jpg", 0)

#x, y = img.shape[:2]


#img_grey = np.zeros([x, y, 3], dtype=np.uint8)



# for i in range(0, x):
#     for j in range(0, y):
#         mean = np.mean(img[i, j])
#         img_grey[i, j] = np.full((1, 3), mean)







cv2.imshow('Original_grey', img)
cv2.waitKey(0)