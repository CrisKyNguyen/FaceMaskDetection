import os
import numpy as np
import time
from sklearn.preprocessing import LabelBinarizer
from tensorflow.keras.utils import to_categorical
from preProcessImage import preProcessImage
import cv2


INPUT_IMAGE_SIZE = (224, 224)

data = []
labels = []
MAIN_DIR = os.path.realpath(os.path.dirname(__file__))
datasetDir = os.path.realpath('./dataset/with-mask_without-mask')
pathFileOut = os.path.realpath('./dataset/dataset.npz')

listFilePath = []
startTime = time.time()

count:int = 0
for dirPath, listDirName, listFileName in os.walk(datasetDir):
    print(count)
    lb = str(count)
    for fileName in listFileName:
        filePath = os.path.realpath(os.path.join(dirPath, fileName))
        img = preProcessImage(cv2.imread(filePath))
        data.append(img)
        labels.append(lb)
    count += 1
    
print('Tổng thời gian xử lý: ',time.time() - startTime)

startTime = time.time()
data = np.array(data, dtype="float32")
labels = np.array(to_categorical(LabelBinarizer().fit_transform(labels)))

np.savez_compressed(pathFileOut, data=data, labels=labels)
print('Tổng thời gian nén và ghi file: ', time.time() - startTime)

print(np.unique(labels))