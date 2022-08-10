import sys
import os
import numpy as np

sys.path.append(
    os.path.realpath(
        os.path.join(
            os.path.dirname(__file__),
            '../'
        )
    )
)
import conf

from modules.preProcessImage import preProcessImage
from modules.loadImageFromDir import loadImageFromDir

def main():
    data, labels, names = loadImageFromDir(datasetDir=conf.DATASET_DIR, preProcessFunc=preProcessImage)

    print('[i] Đang lưu file')
    np.savez_compressed(conf.DATASET_SHARE_FILE, data=data, labels=labels, names=names)
    print('[=>] Lưu file thành công !')

if __name__=='__main__':
    main()