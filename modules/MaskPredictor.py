from tensorflow import keras
from tensorflow.keras import Model
from tensorflow.keras.models import load_model
from modules.preProcessImage import preProcessImage
import numpy as np
import cv2

class MaskPredictor():
    def __init__(self) -> None:
        self.model:Model = None

    def loadModelFromFile(self, filePath:str):
        print(f'[i] Đang thử load model từ file: ')
        print(f'         "{filePath}"')
        try:
            self.model = load_model(filePath)
            print('[=>] Load model thành công !')
        except:
            print(f'[ERROR] Load model từ file: "{filePath}" không thành công !')
            exit()

    def createInput(self, img:np.ndarray, detectResult:tuple) -> np.ndarray:
        listFace = []

        for accuracy, box in detectResult:
            startX, startY, endX, endY = box
            face:np.ndarray = img[startY: endY, startX: endX]
            face = preProcessImage(face)
            listFace.append(face)

        return np.array(listFace, dtype="float32")

    
    def predict(self, img:np.ndarray, detectResult:tuple):
        faces = self.createInput(img, detectResult)
        return self.model.predict(faces, batch_size=32)
