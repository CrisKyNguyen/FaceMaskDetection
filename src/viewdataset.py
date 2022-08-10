import os
import sys
import imutils

sys.path.append(
    os.path.realpath(
        os.path.join(
            os.path.dirname(__file__),
            '../'
        )
    )
)
import conf

import numpy as np
import cv2

def main():
    print('[i] Load dataset từ file: ')
    print(f'     "{conf.DATASET_SHARE_FILE}" ')

    #Load data from share folder
    dataset = np.load(conf.DATASET_SHARE_FILE)
    data = dataset['data']
    labels = dataset['labels']
    names = dataset['names']


    strOldName = 'None'
    oldIndex = 0
    imagesCount = len(data)

    input('[i] Dataset length: ', imagesCount)


    for name in names:

        for i in range(oldIndex, imagesCount):
            strNewName = str(labels[i])
            if strOldName != strNewName:
                strOldName = strNewName
                oldIndex = i
                break
        
        winname = name + '_' + strOldName
        for i in range(oldIndex ,imagesCount):
            img = imutils.resize(data[i], width=400)
            cv2.imshow(winname, mat=img)
            if cv2.waitKey(0) == ord('q'):
                cv2.destroyAllWindows()
                break

if __name__=='__main__':
    main()