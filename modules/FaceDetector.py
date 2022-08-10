import cv2
import os
import numpy as np

class FaceDetector():
    def __init__(self) -> None:
        self.faceNet = None # Face network model
        self.minAccuracy = 0.2 # Độ chính xác tối thiểu


    def setMinAccuracy(self, val):
        self.minAccuracy = val

    # Trả về đường dẫn tất cả các file có phần mở rộng nằm trong list phần mở rộng
    def _getFilePathFromFileNameExtension(self, dirPath:str, listExtension:tuple) -> dict:
        filePath = {}
        
        for fileName in os.listdir(dirPath):
            # Lấy phần mở rộng của tệp
            fileNameExtension = fileName.split('.')[-1].lower()

            if fileNameExtension in listExtension:
                filePath[fileNameExtension] = os.path.join(dirPath, fileName)
            
            if listExtension in filePath:
                break
        
        return filePath
    

    
    # Load face network model từ directory chứa caffe model và tệp mô tả kiến trúc mạng
    # Trả về exception khi xảy ra lỗi
    # Thông báo khi thành công
    def loadFaceNetFromDir(self, dirCaffeDNN:str):
        
        # Get file path
        listExtension = ('prototxt', 'caffemodel')
        print(f'[i] Đang tìm file {str(listExtension)} trong thư mục: ')
        print(f'          "{dirCaffeDNN}" ')

        filePath = self._getFilePathFromFileNameExtension(dirCaffeDNN, listExtension)
        if listExtension != tuple(filePath.keys()):
            print(f'[ERROR]: Không tìm thấy file {str(listExtension)} trong thư mục: "{dirCaffeDNN}" ')
            exit()
        print(f'[=>] Lấy danh sách các file thành công !')

        # Load model
        try:
            print('[i] Đang thử đọc network model từ directory chứa caffe model và tệp mô tả kiến trúc mạng...')
            self.faceNet = cv2.dnn.readNetFromCaffe(filePath['prototxt'], filePath['caffemodel'])
            print('[=>] Đọc network model từ directory chứa caffe model và tệp mô tả kiến trúc mạng thành công !')
        except:
            print(f'[ERROR]: Không thể đọc network model từ thư mục: {str(filePath)} !')
            exit()
        
        

    # Trả về danh sách kết quả
    # (
    #       (
    #           {độ chính xác},
    #           ({startX}, {startY}, {endX}, {endY})
    #       ),
    # )
    def detect(self, img:np) -> tuple:
        #Init
        result:list = []
        (h, w) = img.shape[:2]

        self.faceNet.setInput(
            cv2.dnn.blobFromImage(
                cv2.resize(img, (300, 300)),
                1.0,
                (300, 300),
                (104.0, 177.0, 123.0)
            )
        )

        detections:np.ndarray = self.faceNet.forward()[0, 0]

        for item in detections:
            acccuracy = item[2]
            if acccuracy < self.minAccuracy:
                continue
            
            # Xu ly box
            box = item[3:7]
            box = box*np.array([w,h, w,h])

            startX, startY, endX, endY = box.astype("int")
            startX = max(0, startX)
            startY = max(0, startY)
            endX = min(w - 1, endX)
            endY = min(h - 1, endY)

            box = (startX, startY, endX, endY)
            result.append((acccuracy, box))
        #for
        return tuple(result)
    #def
        


            