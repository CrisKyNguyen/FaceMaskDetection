import os
import numpy as np
import cv2
import time

startTime = time.time()

pathFileOut = os.path.realpath('./dataset/dataset.npz')
loaded = np.load(pathFileOut)

data = loaded['data']
labels = loaded['labels']

lengthOfData = len(data)
print('Tổng lượng hình:', lengthOfData)
print('Tổng thời gian đọc:', time.time()-startTime, 'giây')

for i, img in enumerate(data):
    cv2.imshow(winname=str(labels[i]), mat=img)
    if cv2.waitKey(0) == ord('q'):
        break


for i in range(lengthOfData-1000, lengthOfData):
    cv2.imshow(winname=str(labels[i]), mat=data[i])
    if cv2.waitKey(0) == ord('q'):
        break