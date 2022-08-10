import sys
import os
import cv2
import numpy as np
import imutils
import time
import datetime
import threading

from lapis_modules import formatStr
class SaveImages():
    def __init__(self, fileNameExtension = 'jpg', dirSave:str = '', delay:float = 2) -> None:
        self._fileNameExtension = fileNameExtension
        self._threadSaveImage = None
        self._dirPath = dirSave
        self._delay = delay
        print('[i] Khởi tạo thành công SaveImages')
    
    def _getStrDatetime(self)->str:
        return str(datetime.datetime.now()).replace(':', '-').replace(' ', '_').replace('.', '_')

    def _makeFileName(self, fileName, i:int=0, label:str='') -> str:
        label = label.lower().replace(' ', '_')
        fileName = f'{label}_{fileName}_{formatStr.intNumber(i)}.{self._fileNameExtension}'
        return os.path.join(self._dirPath, fileName)

    # asyn func
    def _saveImage(self, imgs:list = [], label:str='', fileName:str=''):
        for i, img in enumerate(imgs):
            filePath = self._makeFileName(fileName, i, label)
            imgSave = imutils.resize(img.copy(), width=224)
            cv2.imwrite(filePath, imgSave)

        if self._delay > 0:
            time.sleep(self._delay)
    #def

    def notReady(self)->bool:
        return self._threadSaveImage and self._threadSaveImage.is_alive()
    
    def ready(self)->bool:
        return not self.notReady()

    def save(self, imgs: list, label:str='') -> bool:
        if self.notReady():
            return False

        self._threadSaveImage = threading.Thread(
            target = self._saveImage,
            args = (
                imgs,
                label,
                self._getStrDatetime()
            )
        )

        self._threadSaveImage.start()
        return True

    def setDelay(self ,val:float):
        self._delay = val
    
    def getDelay(self) -> float:
        return self._delay

    def setDirSave(self, val):
        self._dirPath = val

    def getDirSave(self)->str:
        return self._dirPath
