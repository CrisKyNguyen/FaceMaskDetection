import os
import sys
sys.path.append(
    os.path.realpath(
        os.path.join(
            os.path.dirname(__file__),
            '../'
        )
    )
)

import conf
import json
import time
import numpy as np
from modules.loadImageFromDir import loadImageFromDir
from modules.preProcessImage import preProcessImage
from modules.modelStruct import createModel
from modules.optimizeData import optimizeData
from sklearn.model_selection import train_test_split


def main():

    #region Model

    # Input 128x128
    # AveragePooling2D(pool_size=(4, 4))  => output_shape = (32, 32)
    # Flatten(name="flatten")  => output_shape = 1024
    # Dense(128, activation="relu")
    # Dropout(0.5)
    # Dense(2, activation="softmax")

    #endregion

    model = createModel()

    #region ModelSummary

    listStrModelSummary = []
    def printSummaryCallback(val:str):
        print(val)
        listStrModelSummary.append(val)
    model.summary(print_fn=printSummaryCallback)

    input('\nNhấn phím enter để tiếp tục: ')
    os.system('cls')

    #endregion ModelSummary

    # Load data from image folder
    if conf.TRAIN_MODEL_FROM_SHARE_DATASET:
        dataset = np.load(conf.DATASET_SHARE_FILE)
        data = dataset['data']
        labels = dataset['labels']
    else:
        data, labels, _ = loadImageFromDir(conf.DATASET_DIR, preProcessFunc=preProcessImage)

    # Load data from share folder
    

    (trainX, testX, trainY, testY) = train_test_split(
        data,
        labels,
        test_size=0.20,
        stratify=labels,
        random_state=42
    )

    trainHistory = model.fit(
        optimizeData().flow(trainX, trainY, batch_size=conf.BATCH_SIZE),
        steps_per_epoch = len(trainX) // conf.BATCH_SIZE,
        validation_data = (testX, testY),
        validation_steps = len(testX) // conf.BATCH_SIZE,
        epochs=conf.EPOCHS
    )

    #region SaveFile

    print('[i] Đang lưu lại model')
    model.save(conf.MODEL_OUT_PATH, save_format="h5")
    print('[i] Save model thành công')


    print('[i] Đang lưu lại history... ')
    f = open(conf.HISTORY_FILE, 'w', encoding='utf-8')
    f.write(json.dumps(trainHistory.history))
    f.close()
    print('[i] Save history thành công')


    print('[i] Đang lưu lại model summary... ')
    f = open(conf.MODEL_SUMMARY_FILE, 'w', encoding='utf-8')
    strModelSummary = '\n'.join(listStrModelSummary)
    f.write(strModelSummary)
    f.close()
    print('[i] Save model summary thành công')

    #endregion

if __name__=='__main__':
    os.system('cls')
    main()