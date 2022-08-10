import os
import numpy as np
import time
import cv2
from  modules.processBar import ProcessBar
from sklearn.preprocessing import LabelBinarizer
from tensorflow.keras.utils import to_categorical


# datasetDir: đường dẫn đầy đủ đến thư mục chứa hình ảnh
# preProcessFunc: Là callback tiền xử lý hình ảnh khi hình ảnh đã được đọc
#        input: np.ndarray => image được đọc từ opencv
#        output: np.ndarray => image sau khi xử lý
# => output: data, label
#           data: là list các image đầu ra đã đc dọc từ thư mục và tiền xử lý bởi callback(preProcessFunc)
#           
def loadImageFromDir(datasetDir, preProcessFunc, displayProcess=False):
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    print('\n[START loadImageFromDir]')
    realFolder = os.path.realpath(datasetDir)

    startTime = time.time()
    data = []
    labels = []
    labelNames = []

    print(f'\n[i] Đang load và xử lý image\n')
    for dirPath, listDirName, listFileName in os.walk(realFolder):
        imageCount = len(listFileName)
        if imageCount == 0:
            continue
        
        processBar = ProcessBar(imageCount)
        lb = dirPath.replace(realFolder, '').replace('\\', '/').strip('/')
        labelNames.append(lb)

        print(f'          + Dir: "{dirPath}"')
        print(f'          + Label: {lb}')
        for i, fileName in enumerate(listFileName):
            filePath = os.path.realpath(os.path.join(dirPath, fileName))
            img = preProcessFunc(cv2.imread(filePath))

            if displayProcess:
                cv2.imshow('loadImageFromDir', img)
                cv2.waitKey(1)

            data.append(img)
            labels.append(lb)
            processBar.next()
            #if
        #for
        print('\n')
    #for

    data = np.array(data, dtype="float32")
    labels = np.array(to_categorical(LabelBinarizer().fit_transform(labels)))

    print(f'[=>] Tổng thời gian xử lý: {round(time.time() - startTime, 4)} giây')
    print(f'[=>] Tổng số image đã load và xử lý: {len(data)} image')
    print(f'[=>] Labels: {str(labelNames)}\n')

    print('[END loadImageFromDir]\n')
    return data, labels, labelNames
#def


## TEST
# from preProcessImage import preProcessImage
# path = 'H:/#A PROJECT/nhan-dang-deo-khau-trang/dataset/with-mask_without-mask'
# loadImageFromDir(path, preProcessFunc=preProcessImage)