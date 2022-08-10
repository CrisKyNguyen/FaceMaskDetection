import cv2
import numpy as np
from tensorflow.keras import preprocessing
from tensorflow.keras.applications import mobilenet_v2
import conf

def preProcessImage(face:np.ndarray)->np.ndarray:
    face = cv2.resize(face, conf.INPUT_IMAGE_SIZE)
    face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
    face = preprocessing.image.img_to_array(face)
    return mobilenet_v2.preprocess_input(face)