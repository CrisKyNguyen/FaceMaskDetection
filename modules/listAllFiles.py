import os
from . import processBar

def listAllFiles(dirPath:str, extensions=None, processDisplay=False):
    #region { init }
    realFolder = os.path.realpath(dirPath)
    result = []
    isTrue = lambda fileName: True
    #endregion

    #region { Gán callback nếu extensions exists }
    if extensions != None and len(extensions) > 0:
        def isTrueFunc(fileName:str):
            fileNameExtension = fileName.split('.')[-1].lower()
            return fileNameExtension in extensions
        isTrue = isTrueFunc
    #endregion

    #region { Process }
    for dirPath, listDirNames, listFileNames in os.walk(realFolder):
        lengthFileNames = len(listFileNames)
        if lengthFileNames == 0:
            continue
        
        print(f'[i] Đang duyệt qua tất cả các file trong thư mục')
        print(f'       "{dirPath}"')

        #region { processBar init }
        if processDisplay:
            STEP = 100/lengthFileNames
            oldCompleted = -1
            newCompleted = 1
        #endregion
        
        listFilePath = []
        for i, fileName in enumerate(listFileNames):
            if isTrue(fileName):
                listFilePath.append(os.path.join(dirPath, fileName))
            #region { print processBar }
            if processDisplay:
                newCompleted = int(i*STEP) + 1
                if newCompleted != oldCompleted:
                    strBar = processBar.strBar(newCompleted)
                    strCompleted = processBar.formatNumber(newCompleted)
                    print(f'\r    Process: {strBar} {strCompleted}% {i}/{lengthFileNames} file', end='')
                    oldCompleted = newCompleted
            #endregion
        #for
        result.extend(listFilePath)

        #region { print processBar }
        if processDisplay:
            strBar = processBar.strBar(newCompleted)
            strCompleted = processBar.formatNumber(newCompleted)
            print(f'\r    Process: {strBar} {strCompleted}% {i}/{lengthFileNames} file')
        #endregion

    #endregion for

    return result
#def

# ##### TESTCASE
# #result = listAllFiles('H:/@ DATA_SET/with-mask_without-mask/with_mask')
# #result = listAllFiles('H:/@ DATA_SET/with-mask_without-mask/with_mask', extensions=('png'))
# #result = listAllFiles('H:/@ DATA_SET/with-mask_without-mask/with_mask', extensions=('png', 'jpg'), processDisplay=True)
# result = listAllFiles('H:/@ DATA_SET/with-mask_without-mask/with_mask', extensions=('png'), processDisplay=True)
# resultCount = len(result)

# maxIndex = 30
# for i, item in enumerate(result):
#     print(item)
#     if i > maxIndex:
#         break

# print('len: ', resultCount)