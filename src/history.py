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
from matplotlib import pyplot as plt
import json

def main():
    # Load history
    f = open(conf.HISTORY_FILE, 'r', encoding='utf-8')
    strHistory = f.read()
    f.close()
    history:dict = json.loads(strHistory)

    # Lấy độ dài nhất của mảng
    maxLength = 0
    for key in history:
        tmp = len(history[key])
        if tmp > maxLength:
            maxLength = tmp
        #if
    #for

    x = [i for i in range(maxLength)]
    listTitle = []
    plt.figure('HISTORY_TRAIN')
    for key in history:
        plt.plot(x ,history[key], label=key)
        listTitle.append(key)


    plt.xlabel('Epoch')
    plt.ylabel('Loss')

    plt.title(', '.join(listTitle))
    plt.legend(loc='best')
    plt.show()

    if input('[?] Save to csv: ').lower() != 'y':
        return
        
    import pandas as pd
    tmpHistory = history.copy()
    for key in tmpHistory:
        for i, item in enumerate(tmpHistory[key]):
            tmpHistory[key][i] = round(item, 4)

    pdHistory = pd.DataFrame.from_dict(tmpHistory)
    print(pdHistory)
    pdHistory.to_csv(conf.OUT_CSV_HISTOTY)
    print('[=>] File đã được lưu lại: ', conf.OUT_CSV_HISTOTY)
    

if __name__ == '__main__':
    main()