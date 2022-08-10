import os

TRAIN_MODEL_FROM_SHARE_DATASET = True

OUT_CSV_HISTOTY = 'out/history.csv'
MAIN_DIR = os.path.dirname(__file__)
MODEL_DIR = './material/model/withMask_withoutMask'

INPUT_IMAGE_SIZE = (128, 128)
#INPUT_IMAGE_SIZE = (224, 224)
INPUT_IMAGE_SHAPE = (INPUT_IMAGE_SIZE[0], INPUT_IMAGE_SIZE[1], 3)


# MAIN ==============================================================================
FACE_CAFFE_DNN_PATH = './material/face_caffe_dnn'

# withMask_withoutMask.model
MODEL_IN_PATH = './material/model/withMask_withoutMask/model.h5'

# Audio
AUDIO_FILE_PATH = './material/audio/alert.wav'

# Key = { [ESC], [Q], [q] }
KEY_STOP = (27, 81, 113)

# cv2.imshow ,,, winname= ????
IMSHOW_WIN_NAME = 'NHAN DIEN KHAU TRANG'

# TRAIN ===============================================================================

# dataset
DATASET_DIR = './dataset/with-mask_without-mask'
DATASET_SHARE_FILE = './dataset_share/with-mask_without-mask.npz'

# OUT
HISTORY_FILE = 'history.json'
MODEL_SUMMARY_FILE = 'summary.txt'
MODEL_OUT_PATH = MODEL_IN_PATH

INIT_LR = 0.0001
EPOCHS = 20
BATCH_SIZE = 32

#region

#Model
FACE_CAFFE_DNN_PATH = os.path.realpath(os.path.join(MAIN_DIR, FACE_CAFFE_DNN_PATH))
MODEL_IN_PATH = os.path.realpath(os.path.join(MAIN_DIR, MODEL_IN_PATH))
MODEL_OUT_PATH = os.path.realpath(os.path.join(MAIN_DIR, MODEL_OUT_PATH))

#Dataset
DATASET_DIR = os.path.relpath(os.path.join(MAIN_DIR, DATASET_DIR))
DATASET_SHARE_FILE = os.path.relpath(os.path.join(MAIN_DIR, DATASET_SHARE_FILE))

AUDIO_FILE_PATH = os.path.realpath(os.path.join(MAIN_DIR, AUDIO_FILE_PATH))

MODEL_DIR = os.path.realpath(os.path.join(MAIN_DIR, MODEL_DIR))
HISTORY_FILE = os.path.realpath(os.path.join(MODEL_DIR, HISTORY_FILE))
MODEL_SUMMARY_FILE = os.path.realpath(os.path.join(MODEL_DIR, MODEL_SUMMARY_FILE))
OUT_CSV_HISTOTY = os.path.realpath(os.path.join(MAIN_DIR, OUT_CSV_HISTOTY))
#endregion