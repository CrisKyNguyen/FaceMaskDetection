BAR_CHAR = chr(9632)
BAR_LENGTH = 30
BAR_STEP = BAR_LENGTH/100
SPACE_CHAR = ' '

def formatNumber(n):
    strN = str(n)
    tmp = 3 - len(strN)
    if tmp > 0:
        return SPACE_CHAR*tmp + strN
    return strN

def strBar(n:int):
    completed = int(n*BAR_STEP)
    return '[' + BAR_CHAR*completed + SPACE_CHAR*(BAR_LENGTH-completed) + ']'


class ProcessBar():
    def __init__(self, maxCount) -> None:
        self._maxCount = maxCount
        self._step = 100/maxCount
        self._oldCompeted = -1
        self._count = 0

    def reset(self):
        self._count = 0
        self._oldCompeted = -1
    
    def next(self):
        self._count += 1
        completed = int(self._step * self._count)
        if completed != self._oldCompeted:
            print(f'\r  Process: {strBar(completed)} {formatNumber(completed)}% {self._count}/{self._maxCount} ', end='')
            self._oldCompeted = completed
    