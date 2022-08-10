import numpy as np
def explodeImage(img:np.ndarray, detectResult, predictResult, callbackIsWithoutMask):
    result = []
    for predict, (accuracy, box) in zip(predictResult, detectResult):
        startX, startY, endX, endY = box
        if callbackIsWithoutMask(predict):
            face = img[startY:endY, startX:endX]
            result.append(face)
    return result
